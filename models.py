from app import db

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    questions = db.relationship('Question', backref='quiz', lazy=True)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_text = db.Column(db.String(200), nullable=False)
    options = db.Column(db.JSON, nullable=False)
    correct_option = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "question_text": self.question_text,
            "options": self.options
        }
