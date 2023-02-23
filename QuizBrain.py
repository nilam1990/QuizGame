class QuizzBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        for i in range(len(self.question_list)):
            current_question = self.question_list[self.question_no]
            self.question_no += 1
            user_answer = input(f"Q.{self.question_no}:{current_question.text} (True/False):")
            if user_answer == current_question.answer:
                self.score += 1
                print(f" You got it ! correct answer is {current_question.answer}")
                print(f" Your current score is {self.score}/12")
            else:
                print(f" You are wrong ! correct answer is {current_question.answer}")
                print(f" Your current score is {self.score}/12")

        return self.score


