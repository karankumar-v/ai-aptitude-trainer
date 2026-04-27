from app import app
from database.db import db
from models.question import Question

with app.app_context():
    q1 = Question(
        question="What is 10 + 5?",
        option1="12",
        option2="15",
        option3="18",
        option4="20",
        answer="15",
        category="aptitude"
    )

    q2 = Question(
        question="What is 20% of 50?",
        option1="5",
        option2="10",
        option3="15",
        option4="20",
        answer="10",
        category="aptitude"
    )

    db.session.add_all([q1, q2])
    db.session.commit()

    print("✅ Questions inserted")