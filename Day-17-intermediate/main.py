from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
if quiz.score >= 10:
    print(f"You're a genius!, you got {quiz.score} points")
elif quiz.score >= 5:
    print(f"You did well, you got {quiz.score} points")
elif quiz.score >= 0:
    print(f"You did poorly, you got {quiz.score} points")
