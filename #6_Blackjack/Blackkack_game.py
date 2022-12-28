# libraries
import random

# /list of cards
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
gameon = ''
# functions
def who_wins(score_player,score_computer):
    if score_player >= 22:
        return "BUST!! You lost :("
    elif score_player > score_computer and score_player <= 21:
        return "You won!!!"
    elif score_player == score_computer and score_player <= 21:
        return "Draw."
    else:
        return "You lost :("

def score(hand):
    score1 = 0
    for i in range(len(hand)):
        score1 += hand[i]
    return score1     

def clear():
    print('\n'*5)
        
# main code      
while gameon != 'n':
    players_score = 0
    computers_cards = []
    computers_score = 0
    players_cards = []
    clear()
    x = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    clear()
    if x == 'y':
        # picking cards
        players_cards = random.choices(cards,k=2)
        computers_card = random.choice(cards)
        computers_cards.append(computers_card)
        players_score = score(players_cards)   
        print(f"Your cards: {players_cards}, current score: {players_score}\nCumputer's first card: {computers_card} ")
        clear()
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'n':
            clear()
            computers_card = random.choice(cards)
            computers_cards.append(computers_card)
            computers_score = score(computers_cards)
            print(f"Your cards: {players_cards}, current score: {players_score}\nCumputer's cards: {computers_cards}, score: {computers_score} ")
            print(who_wins(players_score,computers_score))
        else:
            players_cards.append(random.choice(cards))
            players_score = score(players_cards)
            computers_card = random.choice(cards)
            computers_cards.append(computers_card)
            computers_score = score(computers_cards)
            clear()
            print(f"Your cards: {players_cards}, current score: {players_score}\nCumputer's cards: {computers_cards}, score: {computers_score} ")
            print(who_wins(players_score,computers_score))    
    else:
        gameon = 'n'