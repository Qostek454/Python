from turtle import *


# Constant variables
SNAKE_POSITION = [ (0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
        
    def create_snake(self):    
        for i in SNAKE_POSITION:
            self.add_segment(i)
        
    def add_segment(self, position):    
        snake_part = Turtle(shape='square')
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.parts.append(snake_part)
            
    def extend(self):
        self.add_segment(self.parts[-1].position())
              
            
    
    def move(self):
        for i in range(len(self.parts) - 1, 0, -1): # moving last part of snake to his previous one
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
                      
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)    
