#TODO: asking the question
#TODO: checking if the answer is correct
#TODO: checking if we are the end of the quiz


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0 # adding score value here to calculate the score 
        self.question_list = q_list
        
    def next_question(self):
        current_question = self.question_list[self.question_number] # finding the currect question
        self.question_number += 1
        user_answer = input( f'Q.{self.question_number}: {current_question.text} (True/False)?: ')
        self.check_answer(user_answer, current_question.answer)
        
        
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list) # instead of creating if, use just return 
    
    # adding check_answer method - this method is used in next_question method to define if the user answer is correct
    # user_answer  & correct_answer are used this way because the whole method is used in next_question method 
    # Steps: first - creating a new line in next_qestion method
    #        second - designing the check_answer method
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f'You current score is: {self.score}/{self.question_number}')
        else:
            print(f'You current score is: {self.score}/{self.question_number}')
            print(f'The correct answer is: {correct_answer}')
