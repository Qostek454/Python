from turtle import Turtle, Screen
import pandas


#Variables & dataset
df = pandas.read_csv("C:\\Users\\55599\\Desktop\\Python Portfolio\\#20_U.S_States_Game\\50_states.csv")
image = "C:\\Users\\55599\\Desktop\\Python Portfolio\\#20_U.S_States_Game\\blank_states_img.gif"
game_is_on = True
score = 0

#Screen setups
screen = Screen()
screen.title("U.S. States Game")
screen.addshape(image)
Turtle().shape(image)
mark = Turtle()
mark.hideturtle()
mark.penup()

with open(".\\#20_U.S_States_Game\\my_file.txt", mode = "r") as file2:
    best_score = file2.read()

best_score_mark = Turtle()
best_score_mark.hideturtle()
best_score_mark.penup()
best_score_mark.goto(-400,250)
best_score_mark.write(f'Best Score: {best_score}', font=('Arial',10))


while game_is_on:
    answer = screen.textinput("Guess the State", prompt="What's another state's name?\n To End Game, type end and click on mouse")
    if answer != 'end':
        for i in range(len(df['state'])):
            if df.state[i] == answer:
                score += 1
                x = df.x[i]
                y = df.y[i]
                mark.setpos(x,y)
                mark.write(f"{df.state[i]}")
    else:
        with open(".\\#20_U.S_States_Game\\my_file.txt", mode = "w") as file2:
            file2.write(str(score)) 
        game_is_on = False
        screen.exitonclick()



screen.mainloop()
