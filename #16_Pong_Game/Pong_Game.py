from turtle import *
from random import randint
import time
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard


# Screen setups
screen = Screen()
screen.setup(width = 1000, height = 800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # fixing problem of moving snake (without it all parts of snake moves separately) 


#Objects
paddle_r = Paddle((350,0),5,1)
paddle_l = Paddle((-350,0),5,1)
wall = Paddle((0,330),3,1)
ball = Ball()
scoreboard_paddle_r = Scoreboard((100, 300))
scoreboard_paddle_l = Scoreboard((-100,300))

# Moving paddle by using keyboard keys
screen.listen()
screen.onkey(key = "Up", fun = paddle_r.go_up)
screen.onkey(key = "Down", fun = paddle_r.go_down)
screen.onkey(key = "w", fun = paddle_l.go_up)
screen.onkey(key = "s", fun = paddle_l.go_down)

#Variables
game_is_on = True
ball_speed = 0.1


while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    #Detect colision with floor and ceil
    if ball.ycor() > 280 or ball.ycor() < -280: 
        ball.bounce()
    
    #bouncing of the paddle
    elif ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320 :
        ball.bounce_paddle()
        ball_speed *= 0.9

    #right paddle
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard_paddle_l.add_point()
        ball_speed = 0.1
        
    #left paddle
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard_paddle_r.add_point()
        ball_speed = 0.1
    

screen.exitonclick()