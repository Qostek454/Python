from turtle import *



class Paddle(Turtle): #!!!! to use turle and write code easily 
    # you need to use superclass of Turle
    
    def __init__(self, position,wid,len): #!!!!!! here we input variables that we want to use in main code in line paddle_l = Paddle((350,0))
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=wid,stretch_len=len)
        self.penup()    
        self.setposition(position)

    def go_up(self):
        current_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(current_x,new_y)

    def go_down(self):
        current_x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(current_x,new_y)
    
    def ball(self,position):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.goto(position)
