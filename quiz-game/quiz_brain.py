class quiz_brain:
    def __init__(self, question):
        self.question_num = 0
        self.question_list = question
        self.score = 0

    def still_has_question(self):
        return self.question_num < len(self.question_list)
    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.text} (True/False):  ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            self.score -= 1
            print("Wrong ")
        print(f"Score: {self.score}/{self.question_num} ")
        print(f"The correct answer was: {correct_answer}. ")