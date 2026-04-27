from flask import Flask, render_template, redirect, url_for
from database.db import db
from flask_login import LoginManager, login_required, current_user
from models.user import User
from models.result import Result
from collections import defaultdict
from services.ai_feedback import generate_feedback
from models.ai_question import AIQuestion
from services.ai_feedback import generate_feedback
import requests
from flask import request, jsonify
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# ✅ CREATE APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

# ✅ LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ✅ IMPORT ROUTES AFTER APP CREATION
from routes.auth import auth
from routes.quiz import quiz

app.register_blueprint(auth)
app.register_blueprint(quiz)

# ✅ HOME ROUTE
@app.route('/')
def home():
    return redirect(url_for('auth.login'))


# ai chat
import re

@app.route("/ai-chat", methods=["POST"])
def ai_chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    # 🔒 BASIC FILTER (ALLOW MATH / APTITUDE)
    allowed_keywords = [
        "aptitude", "reasoning", "logical", "probability",
        "percentage", "ratio", "time", "speed", "distance",
        "profit", "loss", "number", "series", "equation"
    ]

    is_math = bool(re.search(r"[0-9+\-*/=]", user_message))

    if not user_message:
        return jsonify({"reply": "Ask me an aptitude question."})

    if not (is_math or any(k in user_message.lower() for k in allowed_keywords)):
        return jsonify({"reply": "I only help with aptitude and reasoning topics."})

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {
                        "role": "system",
                        "content": """
You are an Aptitude Trainer AI.

FORMAT:
1. Explanation
2. Step-by-step solution
3. Final Answer
4. Quick Trick (optional)

Keep it clean, spaced, and structured.
"""
                    },
                    {"role": "user", "content": user_message}
                ]
            }
        )

        data = response.json()
        reply = data["choices"][0]["message"]["content"]

        return jsonify({"reply": reply})

    except Exception as e:
        print("CHAT ERROR:", e)
        return jsonify({"reply": "Error connecting to AI"}), 500

# save-practice
@app.route('/save-practice', methods=['POST'])
@login_required
def save_practice():
    data = request.get_json()

    new_result = Result(
        user_id=current_user.id,
        score=data['score'],
        total_questions=data['total'],
        category=data['category']
    )

    db.session.add(new_result)
    db.session.commit()

    return jsonify({"status": "success"})

#generate weakarea question
@app.route('/generate-weak-questions', methods=['POST'])
@login_required
def generate_weak_questions():
    from services.ai_service import generate_questions

    data = request.get_json()

    topic = data.get("topic")
    difficulty = data.get("difficulty")

    questions = generate_questions(topic, difficulty)

    return jsonify({"questions": questions})
    
# ✅ DASHBOARD (FULL FIXED)
@app.route('/dashboard')
@login_required
def dashboard():
    from services.ai_feedback import generate_feedback
    from datetime import datetime, timedelta

    results = Result.query.filter_by(user_id=current_user.id).all()

# ✅ ALWAYS DEFINE FIRST
    scores = []
    dates = []

    total_quizzes = len(results)
    total_q = sum(r.total_questions for r in results)
    total_score = sum(r.score for r in results)

    avg_score= round((total_score / total_q) * 100, 2) if total_q else 0
    # DEFAULT VALUES
    weak_area = "No Data Yet"
    mistake_type = "N/A"
    ai_feedback = "Start practicing quizzes to get AI feedback."
    streak = 0

    scores = []
    dates = []   # ✅ FIXED (rename from dates → labels)

    if results:   # ✅ FIXED (simpler condition)

        category_stats = {}

        for r in results:
            scores.append(r.score)
            dates.append(r.timestamp.strftime("%d-%m"))

            if not r.category or r.total_questions == 0:
                continue

            if r.category not in category_stats:
                category_stats[r.category] = {"score": 0, "total": 0}

            category_stats[r.category]["score"] += r.score
            category_stats[r.category]["total"] += r.total_questions

        if category_stats:
            lowest_acc = 1

            for cat, data in category_stats.items():
                if data["total"] == 0:
                    continue

                acc = data["score"] / data["total"]

                if acc < lowest_acc:
                    lowest_acc = acc
                    weak_area = cat

            mistake_type = "Careless Mistakes" if avg_score < 0.6 else "Conceptual Errors"

            # ✅ REAL AI FEEDBACK CALL
            ai_feedback = generate_feedback(weak_area, mistake_type, avg_score)

        # 🔥 STREAK LOGIC (SAFE)
        today = datetime.utcnow().date()
        attempt_dates = sorted(
            [r.timestamp.date() for r in results if r.timestamp],
            reverse=True
        )

        for i, d in enumerate(attempt_dates):
            if i == 0:
                if d == today or d == today - timedelta(days=1):
                    streak = 1
                else:
                    break
            else:
                if attempt_dates[i-1] - d == timedelta(days=1):
                    streak += 1
                else:
                    break

    return render_template(
    "dashboard.html",
    total_quizzes=total_quizzes,
    avg_score=round(avg_score, 2),
    weak_area=weak_area,
    mistake_type=mistake_type,
    results=results,
    ai_feedback=ai_feedback,
    scores=scores if scores else [],
    dates=dates if dates else [],
    streak=streak
)
# ✅ leaderboard route
@app.route('/leaderboard')
@login_required
def leaderboard():
    from models.result import Result
    from models.user import User
    from sqlalchemy import func

    leaderboard_data = db.session.query(
        User.username,
        func.sum(Result.score).label("total_score"),
        func.sum(Result.total_questions).label("total_questions")
    ).join(User, User.id == Result.user_id)\
     .group_by(User.username)\
     .order_by(func.sum(Result.score).desc())\
     .all()

    return render_template("leaderboard.html", leaderboard=leaderboard_data)
    

# ✅ RUN APP
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)