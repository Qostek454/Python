from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()    
        self.setposition(STARTING_POSITION)
        self.left(90)

    def move(self):
        new_y = self.ycor() + 20
        self.goto(0,new_y)

    def reset_starting_position(self):
        self.penup()
        self.setposition(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
