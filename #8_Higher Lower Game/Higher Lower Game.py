from art import logo, vs
from game_data import data
import random

print(logo)


# variables
#gameon = False
#a = random.choice(list(data))
#b = random.choice(list(data))
#points = 0
 
def game(): 
    a = random.choice(list(data))
    b = random.choice(list(data))
    gameon = False
    points = 0
    while gameon != True:
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs,"\n")
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        player_choice = input("\nWho has more followers? Type 'a' or 'b': ")
        if player_choice == 'a' and a['follower_count'] >= b['follower_count']:
            points += 1
            print(f'\nYour points: {points}')
        elif player_choice == 'b' and a['follower_count'] < b['follower_count']:
            a = b
            points += 1
            print(f'\nYour points: {points}')
        else:
            print(f'\nYou lose :( Your final score is: {points}')
            break
        b = random.choice(list(data))

        

game()
