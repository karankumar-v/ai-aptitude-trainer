from database.db import db
from datetime import datetime

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    score = db.Column(db.Integer)
    total_questions = db.Column(db.Integer)  # NEW
    category = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)