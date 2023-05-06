class QuizLogic:
    
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        

    def ask_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        
    
    def still_has_question(self):
        return  len(self.question_list) > self.question_number
            
    
    def check_answer(self, user_answer, current_question_answer):
        if user_answer.lower() == current_question_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You didn't get it right!!'")
        print(f"The correct answer was: {current_question_answer}.")
        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")