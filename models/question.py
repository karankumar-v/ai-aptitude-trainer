from database.db import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    question = db.Column(db.Text, nullable=False)

    option1 = db.Column(db.String(255))
    option2 = db.Column(db.String(255))
    option3 = db.Column(db.String(255))
    option4 = db.Column(db.String(255))

    answer = db.Column(db.String(255))

    category = db.Column(db.String(100))
    topic = db.Column(db.String(50))
    difficulty = db.Column(db.String(20))
    difficulty = db.Column(db.String(50), default="easy")  # ✅ ADD THIS