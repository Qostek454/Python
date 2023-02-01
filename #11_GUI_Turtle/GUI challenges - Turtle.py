from turtle import * # * importing everything that is in turtle module
from random import randint, randrange, choice

timmy = Turtle()

#Task1: Draw shapes traingle square etc
timmy.shape("circle")
colormode(255)
for i in range(3,11):
    timmy.color((randint(0,255),randint(0,255),randint(0,255)))
    for _ in range(i):
        timmy.forward(100)
        timmy.right(360 / i)


#Task2: Random walk
timmy.shape("circle")
timmy.pensize(10)
timmy.speed(50)
colormode(255)

for _ in range(100):
    timmy.color((randint(0,255),randint(0,255),randint(0,255))) # random color
    timmy.forward(10)
    direction = [0,90,180,270]
    timmy.right(choice(direction))

#Task3: Draw a Spirograph
timmy.shape("circle")
timmy.pensize(1)
timmy.speed(25)
colormode(255)
i = 1

while i <= 360:
    timmy.color((randint(0,255),randint(0,255),randint(0,255)))
    timmy.circle(100)
    timmy.left(i)
    i += 1

# closing window
screen = Screen()
screen.exitonclick()

