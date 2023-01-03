import random
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
game_level = input("Choose a difficulty. Type 'easy' or hard: ")

chosen_number = random.randrange(1,100)
result = False


def compare_numbers(player_number,computer_number):
    """Check numbers"""
    result = False
    if player_number > computer_number:
            print("Too high.\nGuess again.")
            return result 
    elif player_number < computer_number:
            print("Too low.\nGuess again.")
            return result 
    elif player_number == computer_number:    
            print("You guessed the number!! HuRRa!")
            result = True
            return result
    

if game_level == 'easy':
    numb_of_attemps = 10
    while result != True:
        print(f"You have {numb_of_attemps} attemps remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        numb_of_attemps -= 1
        if compare_numbers(user_guess,chosen_number) == True:
            result = True    
        if numb_of_attemps == 0:
            print(f"\nYou run out of attemps. You lose. :(\n\nThe correct number was: {chosen_number}")
            result = True
            
elif game_level == 'hard':
    numb_of_attemps = 5
    while result != True:
        print(f"You have {numb_of_attemps} attemps remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        numb_of_attemps -= 1
        if compare_numbers(user_guess,chosen_number) == True:
            result = True    
        if numb_of_attemps == 0:
            print(f"\nYou run out of attemps. You loose. :(\n\nThe correct number was: {chosen_number}")
            result = True
else:
    print("Wrong game difficulty.")