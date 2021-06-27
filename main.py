from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank =[]
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz=Quiz(question_bank)

while quiz.next(): 
    quiz.next_question()

print("You completed the quiz")
print(f"The result : {quiz.score}/{len(question_bank)}")
