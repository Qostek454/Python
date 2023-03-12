import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#Objects
player = Player() #size 20x20
car = CarManager() #size 20x40
scoreboard = Scoreboard()
    
# moving turtle
screen.listen()
screen.onkey(key = "Up", fun = player.move)


game_is_on = True
car_speed = 0.1

while game_is_on:
    time.sleep(car_speed)
    screen.update()

    # creating cars
    car.create_car()
    car.move_car()

    # Reaching next level
    if player.is_at_finish_line():
        player.reset_starting_position()
        scoreboard.add_point()
        car_speed *= 0.9
    
    # hiting with car
    for i in car.all_cars: # looping throu all the car that are in all_cars list
        if i.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()



