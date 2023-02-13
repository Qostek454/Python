from turtle import *
from random import randint

# Variables
is_race_on = False
colors = ["red","orange","yellow","green","blue","purple"]
y_start_position = -80
screen = Screen()
screen.setup(width = 500,height = 400)
userbet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
all_turtles = []

# Going to start line
for turtle in range(len(colors)):
    turt = Turtle(shape = "turtle")
    turt.color(colors[turtle])
    turt.penup()
    turt.goto(x = -238, y = y_start_position)
    y_start_position += 40
    all_turtles.append(turt)


# Starting race
if userbet:
    is_race_on = True

# Let's race
while is_race_on:
   
    for i_turtle in all_turtles:
        if i_turtle.xcor() > 230:
            winning_turtle_color = i_turtle.pencolor()
            if winning_turtle_color == userbet:
                print("You won!!!!")
            else:
                print(f'You lost. {i_turtle.pencolor()} won the race.')        
            is_race_on = False
        rand_distance = randint(0, 10)
        i_turtle.forward(rand_distance)

screen.exitonclick()