from turtle import *
from random import randint
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

# Screen setups
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # fixing problem of moving snake (without it all parts of snake moves separately) 



#1  Create 3-part Snake (Task 1: Create snake)
    
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#2 Move the snake (Task 2: Move snake)
screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

#3 Playing snake
game_is_on = True


while game_is_on:
    screen.update() # showing the snake / snake is moving as one pice
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food)< 15: #Detect colision with food
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    if    snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: # deteco colision with wall
            game_is_on = False
            scoreboard.game_over()
            
    for i in snake.parts[1:]:
        if snake.head.distance(i) < 10: 
           game_is_on = False
           scoreboard.game_over()
            
screen.exitonclick()