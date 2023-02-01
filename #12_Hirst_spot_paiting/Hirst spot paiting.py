from turtle import *
from random import randint, randrange, choice

# Functions
def line_of_spots(number_of_spots,distance_between_spots):
    """This function creates a chosen numbers of color-filled circle in a line"""
    for _ in range(number_of_spots):
        # chosing color and coloring the cirle
        random_color = (randint(0,255),randint(0,255),randint(0,255))
        mark.dot(20,random_color)
        # moving forward
        mark.penup()
        mark.forward(distance_between_spots)
        mark.pendown()

def hirst_spot_paiting(number_of_lines,number_of_spots,x_position,y_position, distance_between_lines,distance_between_spots):
    for _ in range(number_of_lines):
        mark.penup()
        mark.setpos(x_position,y_position)
        mark.left(90)
        mark.penup()
        mark.forward(distance_between_lines)
        mark.pendown()
        mark.right(90)
        line_of_spots(number_of_spots,distance_between_spots)
        y_position += 50
    mark.hideturtle()
# Settings - turtle
mark = Turtle()
mark.shape('arrow')
mark.pensize(1)
mark.speed(25)
colormode(255)

 # hirst_spot_paiting    
hirst_spot_paiting(10,10,-200,-200,50,50)    


# Settings - screen
screen = Screen()
screen.exitonclick()