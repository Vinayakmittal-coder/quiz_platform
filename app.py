from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models
from models import Quiz, Question

@app.route('/quizzes', methods=['GET'])
def get_quizzes():
    quizzes = Quiz.query.all()
    return jsonify([quiz.to_dict() for quiz in quizzes])

@app.route('/quiz/<int:quiz_id>', methods=['GET'])
def get_quiz_questions(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return jsonify([question.to_dict() for question in quiz.questions])

@app.route('/quiz/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    data = request.json
    score = 0
    for response in data['responses']:
        question = Question.query.get(response['question_id'])
        if question.correct_option == response['answer']:
            score += 1
    return jsonify({'score': score})

if __name__ == "__main__":
    app.run(debug=True)
