from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


# Creating question_bank
question_bank = []
for i in range(len(question_data)):
    question = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(question)
    
 
quiz = QuizBrain(question_bank)    

while quiz.still_has_questions():
    quiz.next_question()   
    
# ending words and score    
print("You've complated the quiz. Congratulations!")
print(f'Your final score is: {quiz.score}/{quiz.question_number}')
print("Good Bye!")
