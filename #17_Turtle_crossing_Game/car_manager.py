from turtle import *
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple","dark blue","dark green","black"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):    
        random_number = random.randint(1,4) # using it to descrease the number of cars in game
        if random_number == 1:
            car = Turtle(shape='square')
            car.color(COLORS[random.randint(0,8)])
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.left(180)
            random_y = random.randint(-250,250)
            car.goto(300,random_y)
            self.all_cars.append(car)
            
    def move_car(self):
        for i in self.all_cars:
            new_x = i.xcor() - MOVE_INCREMENT
            y = i.ycor()
            i.goto(new_x, y)
    
