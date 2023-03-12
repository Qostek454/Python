from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.scoreboard = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-270,280)
        self.write(f"Level: {self.scoreboard}", False, align = "center", font=('Arial', 10,'bold'))
        
        
    def add_point(self):
        self.scoreboard += 1
        self.clear()
        self.write(f"Level: {self.scoreboard}", False, align = "center", font=('Arial', 10,'bold'))
        
    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.color("black")
        self.write(f" GAME OVER ", False, align = "center", font=('Arial', 15,'bold'))
        self.penup()
        self.hideturtle()
        self.goto(0,-20)
        self.write(f"Level: {self.scoreboard}", False, align = "center", font=('Arial', 10,'bold'))
