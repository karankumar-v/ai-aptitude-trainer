import requests
import json

API_KEY = "YOUR_OPENROUTER_API_KEY"

def generate_questions(topic, difficulty):
    prompt = f"""
Generate 10 multiple choice aptitude questions.

Topic: {topic}
Difficulty: {difficulty}

Return ONLY valid JSON like this:
[
  {{
    "question": "text",
    "options": ["A","B","C","D"],
    "answer": "correct option text"
  }}
]
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    data = response.json()

    try:
        content = data["choices"][0]["message"]["content"]

        # 🔥 Extract JSON safely
        start = content.find("[")
        end = content.rfind("]") + 1
        json_str = content[start:end]

        return json.loads(json_str)

    except Exception as e:
        print("AI ERROR:", e)
        return []