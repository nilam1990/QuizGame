from data import question_data
from QuestionModel import Question
from QuizBrain import QuizzBrain
question_bank = []


for item in question_data:
    new_q = Question(item["text"], item["answer"])
    question_bank.append(new_q)
print(question_bank)


quizz = QuizzBrain(question_bank)
final_score = quizz.next_question()
print(f"Your Final Score is {final_score}/12")



'''
for obj in question_bank:
    obj.display_data()
'''


