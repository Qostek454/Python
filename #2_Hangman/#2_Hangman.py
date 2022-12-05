#Libraries
import random

# importing lists from other workbooks
from hangman_words_list import word_list
from hangman_logos import logo
from hangman_logos import stages


# Variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = [] # showing guessed letters
end_of_game = False
lives = 6

print(logo)


# Creating blank word
for _ in range(word_length):
    display += "_"

# loop till the game is over / choose letter
while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()

    # Check if guessed letter is in chosen word
    for i in range(word_length):
        if chosen_word[i] == guess_letter:
            display[i] = chosen_word[i]

    #Check if user is wrong and print the information
    if guess_letter not in chosen_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        # Take one choice from user
        lives -= 1
        # check if user has still choices
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has guessed all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Printing stages after every guess
    print(stages[lives])