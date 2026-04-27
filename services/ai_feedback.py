import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_feedback(weak_area, mistake_type, avg_score):

    # ✅ SAFETY CHECK
    if not weak_area or not mistake_type:
        return "Start practicing to get AI feedback."

    prompt = f"""
You are an aptitude coach.

Weak Area: {weak_area}
Mistake Type: {mistake_type}
Score: {avg_score}

Give output in this format:

1. Problem:
(short)

2. Why:
(short)

3. Fix:
- Step 1
- Step 2
- Step 3

4. Tip:
(one line)
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
                "messages": [
                    {"role": "user", "content": prompt.strip()}
                ]
            }
        )

        data = response.json()

        # 🔍 DEBUG PRINT
        if "choices" not in data:
            print("AI FEEDBACK ERROR:", data)
            return "AI feedback unavailable."

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("FEEDBACK EXCEPTION:", e)
        return "AI feedback unavailable."