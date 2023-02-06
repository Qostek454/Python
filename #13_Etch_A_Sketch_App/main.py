from turtle import *


mark = Turtle()
screen = Screen()


# Functions - move forwards/bacwards, turn left/right, clear screen
def turn_right():
    mark.right(10)

def turn_left():
    mark.left(10)

def move_forward():
    mark.forward(10)
    
def move_backward():
    mark.backward(10)
    
def clear_drawing():
    mark.reset()
    
    
#  Rocking around mark
screen.listen()
screen.onkey(key = 'a', fun = turn_left)
screen.onkey(key = 'w', fun = move_forward)
screen.onkey(key = 'd', fun = turn_right)
screen.onkey(key = 's', fun = move_backward)
screen.onkey(key = 'c', fun = clear_drawing)
screen.exitonclick()

