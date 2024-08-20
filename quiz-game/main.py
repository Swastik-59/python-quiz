from question_model import question_model as Questions
from data import question_data
from quiz_brain import quiz_brain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Questions(question_text , question_answer)
    question_bank.append(new_question)

quiz = quiz_brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
