
class QuizBrain():
    def __init__(self, q_list: list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        if answer == self.current_question.answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
 
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
    
        

