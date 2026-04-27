import requests
import json
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# ✅ 1. GENERATE QUESTIONS (USED BY QUIZ)
def generate_questions(category, difficulty, topic=None):

    topic_line = f"Topic: {topic}" if topic else ""

    prompt = """
Generate 10 multiple choice questions.

Category: {category}
Difficulty: {difficulty}
{topic_line}

Rules:
- ONLY aptitude, logical, reasoning, verbal
- NO general knowledge
- Questions must be numerical or logic-based
- Include step-by-step explanation

Format:
[
  {{
    "question": "...",
    "options": ["A","B","C","D"],
    "answer": "...",
    "explanation": "Step 1: ...\\nStep 2: ...\\nFinal Answer: ..."
  }}
]
""".format(category=category, difficulty=difficulty, topic_line=topic_line)
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "temperature": 0.3,
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        data = response.json()
        content = data["choices"][0]["message"]["content"]

        # extract JSON safely
        start = content.find("[")
        end = content.rfind("]") + 1
        json_str = content[start:end]

        return json.loads(json_str)

    except Exception as e:
        print("AI QUESTION ERROR:", e)
        return []


# ✅ 2. CHATBOT (CLEAN OUTPUT)
def aptitude_chat(user_input):
    if not user_input or user_input.strip() == "":
        return "Ask a valid aptitude question."

    prompt = f"""
You are an aptitude trainer.

STRICT RULES:
- Only aptitude / reasoning / math
- No paragraphs
- No explanation headings
- No markdown

FORMAT:

Step 1: ...
Step 2: ...
Step 3: ...

Final Answer: ...

Question:
{user_input}
"""

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "temperature": 0.2,
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        data = response.json()
        text = data["choices"][0]["message"]["content"]

        # cleanup
        text = text.replace("**", "")
        text = text.replace("Explanation", "")
        text = text.replace("Solution", "")

        return text.strip()

    except Exception as e:
        print("CHAT ERROR:", e)
        return "Error generating response"


# ✅ 3. AI FEEDBACK
def generate_feedback(weak_area, mistake_type, avg_score):
    prompt = f"""
You are an aptitude coach.

No paragraphs. Keep it clean.

FORMAT:

Problem:
...

Why:
...

Fix:
Step 1: ...
Step 2: ...
Step 3: ...

Tip:
...

DATA:
Weak Area: {weak_area}
Mistake: {mistake_type}
Score: {avg_score}
"""

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "temperature": 0.2,
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        data = response.json()
        text = data["choices"][0]["message"]["content"]

        # cleanup numbering
        text = text.replace("1.", "").replace("2.", "").replace("3.", "")

        return text.strip()

    except Exception as e:
        print("FEEDBACK ERROR:", e)
        return "AI feedback unavailable."