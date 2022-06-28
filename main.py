from question_model import Question
from data import question_data
from quiz_brain import Quiz


question_bank = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

new_quiz = Quiz(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print(" Your quiz has completed !")
print(f" Your Final Score is {new_quiz.score}/{len(new_quiz.question_list)}")
    
