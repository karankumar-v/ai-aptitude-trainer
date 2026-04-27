from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from database.db import db

from models.question import Question
from models.result import Result
from models.ai_question import AIQuestion
from services.ai_service import generate_questions, aptitude_chat, generate_feedback
quiz = Blueprint('quiz', __name__)

# ---------------- NORMAL QUIZ ---------------- #

@quiz.route('/quiz')
@login_required
def quiz_page():
    category = request.args.get('category')
    topic = request.args.get('topic')
    difficulty = request.args.get('difficulty')

    query = Question.query

    # ✅ Apply filters only if selected
    if category and category != "all":
        query = query.filter_by(category=category)

    if topic and topic != "all":
        query = query.filter_by(topic=topic)

    if difficulty and difficulty != "all":
        query = query.filter_by(difficulty=difficulty)

    questions = query.limit(5).all()

    return render_template(
        'quiz.html',
        questions=questions,
        category=category,
        topic=topic,
        difficulty=difficulty
    )

@quiz.route('/submit_quiz', methods=['POST'])
@login_required
def submit_quiz():
    category = request.form.get('category')

    score = 0
    total = 0

    for key in request.form:
        if key == "category":
            continue

        q = Question.query.get(int(key))
        if not q:
            continue

        total += 1
        user_answer = request.form.get(key)

        if user_answer == q.answer:
            score += 1

    if total == 0:
        return "No questions submitted."

    result = Result(
        user_id=current_user.id,
        score=score,
        total_questions=total,
        category=category
    )

    db.session.add(result)
    db.session.commit()

    return redirect(url_for('dashboard'))


# ---------------- AI PRACTICE (MANUAL UI PAGE) ---------------- #

@quiz.route('/ai-practice')
@login_required
def ai_practice():
    return render_template(
        "practice.html",
        weak_area="General Aptitude",
        difficulty="medium"
    )

# ---------------- Reset all data---------------- #
@quiz.route('/reset-data', methods=['POST'])
@login_required
def reset_data():
    # delete user results
    Result.query.filter_by(user_id=current_user.id).delete()

    # delete AI questions
    AIQuestion.query.delete()

    db.session.commit()

    return redirect(url_for('dashboard'))

# ---------------- SMART PRACTICE ---------------- #

@quiz.route('/practice-weak-area')
@login_required
def practice_weak_area():
    results = Result.query.filter_by(user_id=current_user.id).all()

    category_stats = {}

    VALID_CATEGORIES = ["aptitude", "logical", "reasoning", "verbal"]

    for r in results:
        if r.category not in VALID_CATEGORIES:
         continue  # 🚫 skip "mixed" or garbage data

        if r.category not in category_stats:
         category_stats[r.category] = {"score": 0, "total": 0}

         category_stats[r.category]["score"] += r.score
         category_stats[r.category]["total"] += r.total_questions
    # DEFAULT
    if not category_stats:
        weak_area = "aptitude"
        difficulty = "easy"
    else:
        weak_area = None
        lowest_acc = 1

        for cat, data in category_stats.items():
            if data["total"] == 0:
                continue

            acc = data["score"] / data["total"]

            if acc < lowest_acc:
                lowest_acc = acc
                weak_area = cat

        if weak_area is None:
            weak_area = "aptitude"

        total = category_stats.get(weak_area, {}).get("total", 0)
        score = category_stats.get(weak_area, {}).get("score", 0)

        avg_accuracy = (score / total) if total > 0 else 0

        if avg_accuracy < 0.4:
            difficulty = "easy"
        elif avg_accuracy < 0.75:
            difficulty = "medium"
        else:
            difficulty = "hard"

    # 🔥 IMPORTANT: CLEAR OLD QUESTIONS BEFORE ADDING NEW ONES
    AIQuestion.query.delete()
    db.session.commit()

    # 🤖 Generate AI questions
    ai_data = generate_questions(weak_area, difficulty)

    saved_questions = []

    for q in ai_data:
        options = q["options"]
        answer_text = q["answer"]

        correct_letter = "A"

        for i, opt in enumerate(options):
            if opt.strip() == answer_text.strip():
                correct_letter = ["A", "B", "C", "D"][i]
                break

        new_q = AIQuestion(
    category=weak_area,
    question=q["question"],
    option_a=options[0],
    option_b=options[1],
    option_c=options[2],
    option_d=options[3],
    correct_answer=correct_letter,
    explanation=q.get("explanation", "No explanation provided")
)

        db.session.add(new_q)
        saved_questions.append(new_q)

    db.session.commit()

    return render_template(
        "ai_quiz.html",
        questions=saved_questions,
        category=weak_area,
        difficulty=difficulty,
        mode="smart"
    )


# ---------------- SUBMIT AI QUIZ ---------------- #

@quiz.route('/submit-ai-quiz', methods=['POST'])
@login_required
def submit_ai_quiz():

    # 🔥 GET ONLY SUBMITTED QUESTION IDS
    question_ids = request.form.getlist("questions")

    score = 0
    results = []

    for qid in question_ids:
        q = AIQuestion.query.get(int(qid))
        if not q:
            continue

        user_answer = request.form.get(f"q{q.id}")

        answer_map = {
            "A": q.option_a,
            "B": q.option_b,
            "C": q.option_c,
            "D": q.option_d
        }

        correct_text = answer_map.get(q.correct_answer)

        if not user_answer:
            is_correct = False
            user_answer_display = None
        else:
            is_correct = (user_answer == correct_text)
            user_answer_display = user_answer

        if is_correct:
            score += 1

        results.append({
    "question": q.question,
    "options": [q.option_a, q.option_b, q.option_c, q.option_d],
    "user_answer": user_answer_display,
    "correct_answer": correct_text,
    "is_correct": is_correct,
    "explanation": q.explanation
})
    total = len(results)

    # cleanup
    AIQuestion.query.delete()
    db.session.commit()

    return render_template(
        "ai_result.html",
        score=score,
        total=total,
        results=results
    )