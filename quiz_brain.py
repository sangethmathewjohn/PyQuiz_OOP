class Quiz:
    def __init__(self,qlist):
        self.question_numbers =0
        self.score =0
        self.question_list =qlist
    
    def next(self):
        return self.question_numbers<len(self.question_list)
         

    def next_question(self):
        current_question = self.question_list[self.question_numbers]
        self.question_numbers+=1
        user =input(f"Q.{self.question_numbers}: {current_question.text}? ('True' or' False') ")
        self.check(user,current_question.answer)
        

    def check(self,user,correct):
        if user.lower() == correct.lower():
            print("You got it right !!!")
            self.score +=1
        else:
            print("You were wrong")
        print(f"The correct answer is {correct}")
        print (f"Your score is {self.score}/{self.question_numbers}")
        print ("\n \n")

