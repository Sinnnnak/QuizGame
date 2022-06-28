class Quiz:
    
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0
        
    def still_has_questions(self):
        return self.question_no < len(self.question_list) 
        
    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no }: {question.question} (True / False)? :")
        correct_answer = question.answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right !")
            self.score += 1
        else:
            print("Wrong Answer !")
        print(f"Your Correct answer was {correct_answer}")
        print(f"Your Final Score is {self.score} / {self.question_no}")
            