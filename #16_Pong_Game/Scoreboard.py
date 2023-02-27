from turtle import *


class Scoreboard(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.scoreboard = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"{self.scoreboard}", False, align = "center", font=('Arial', 40,'bold'))
        
        
    def add_point(self):
        self.scoreboard += 1
        self.clear()
        self.write(f" {self.scoreboard}", False, align = "center", font=('Arial', 40,'bold'))
        
    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write(f" GAME OVER ", False, align = "center", font=('Arial', 15,'normal'))
        self.penup()
        self.hideturtle()
        self.goto(0,-20)
        self.write(f"Scoreboard: {self.scoreboard}", False, align = "center", font=('Arial', 10,'normal'))