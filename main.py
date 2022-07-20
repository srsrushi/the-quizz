from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for qa in question_data:
    question = Question(qa["question"], qa["correct_answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
