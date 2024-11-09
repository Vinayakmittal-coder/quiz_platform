from app import db
from models import Quiz, Question

def populate_data():
    db.create_all()

    quiz1 = Quiz(title="Python Basics", description="Test your Python knowledge.")
    db.session.add(quiz1)
    db.session.commit()

    questions = [
        Question(
            quiz_id=quiz1.id,
            question_text="What is the output of print(2**3)?",
            options=["6", "8", "9", "None of these"],
            correct_option="8"
        ),
        Question(
            quiz_id=quiz1.id,
            question_text="What data type is returned by input() in Python?",
            options=["int", "str", "float", "None"],
            correct_option="str"
        ),
    ]
    db.session.bulk_save_objects(questions)
    db.session.commit()

if __name__ == "__main__":
    populate_data()
