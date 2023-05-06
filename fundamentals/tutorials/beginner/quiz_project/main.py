from question_model import Question
from data import question_data
from quiz_logic import QuizLogic


question_bank = []

for question in question_data:
    new_question_model = Question(question['text'], question['answer'])
    question_bank.append(new_question_model)
    # print(question_bank)


quiz = QuizLogic(question_bank)

while quiz.still_has_question():
    quiz.ask_question()

print("You've completed the quiz")
print (f"Your final score was: {quiz.score}/{quiz.question_number}")