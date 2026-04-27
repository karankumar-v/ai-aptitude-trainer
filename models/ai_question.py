from database.db import db

class AIQuestion(db.Model):
    __tablename__ = 'ai_question'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    question = db.Column(db.Text)

    option_a = db.Column(db.String(255))
    option_b = db.Column(db.String(255))
    option_c = db.Column(db.String(255))
    option_d = db.Column(db.String(255))

    correct_answer = db.Column(db.String(10))
    explanation = db.Column(db.Text)