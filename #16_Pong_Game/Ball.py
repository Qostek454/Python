from turtle import *


class Ball(Turtle): #!!!! to use turle and write code easily 
    # you need to use superclass of Turle
    
    def __init__(self): #!!!!!! here we input variables that we want to use in main code in line paddle_l = Paddle((350,0))
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()    
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    
    def bounce_paddle(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.goto(0,0)
        self.bounce_paddle()


        
