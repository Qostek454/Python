# day 15 of course
# 1. Print report.
# 2. Check resources sufficient?
# 3. Process coins.
# 4. Check transaction successful?
# 5. MAke Coffee.
# 6. refill resources
# 7. Notify if there is no chance to make chosen drink!

from Recipies import MENU, resources

question = ""
resources['Money'] = 0

# functions
def coins():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    inserted_coins = quarters + dimes + nickles + pennies
    return inserted_coins

def updating_resources(drink):
    resources['water'] =  resources['water'] - MENU[drink]['ingredients']['water']
    resources['milk'] =  resources['milk'] - MENU[drink]['ingredients']['milk']
    resources['coffee'] =  resources['coffee'] - MENU[drink]['ingredients']['coffee']
    
def refill_resources():
    water = int(input("How much water do you add? "))
    milk = int(input("How much milk do you add? "))
    coffee = int(input("How much coffee do you add? "))
    resources['water'] =  resources['water'] + water
    resources['milk'] =  resources['milk'] + milk
    resources['coffee'] =  resources['coffee'] + coffee
    
def resource_status(drink):
    if resources['water'] < MENU[drink]['ingredients']['water']:
        print("Sorry, there is not enough water. Please come back later. Thank you!")
        return False
    elif resources['milk'] < MENU[drink]['ingredients']['milk']:
        print("Sorry, there is not enough milk. Please come back later. Thank you!")
        return False
    elif resources['coffee'] < MENU[drink]['ingredients']['coffee']:
        print("Sorry, there is not enough coffee. Please come back later. Thank you!")
        return False
    else:
        return True
        


# main code
while question != 'off':
    question = input("“What would you like? (espresso/latte/cappuccino): ")
    if question == 'off':
        break
    elif question == 'report':
        print(resources)
    elif question == 'add':
        refill_resources()  
        print(resources)
    else:
        if resource_status(question) == False:
            continue
        else:
            print(f"{question.capitalize()} costs ${MENU[question]['cost']}.")
            confirmation = input(f"Do you want {question.capitalize()}? Type 'yes' or 'no'.: ")
            if confirmation == 'no':
                continue
            else:
                sum_coins = float(coins())
                print(f"You inserted ${sum_coins}.")
                if sum_coins >= MENU[question]['cost']:
                    change = sum_coins - float(MENU[question]['cost'])
                    resources['Money'] = resources['Money'] + MENU[question]['cost']
                    updating_resources(question)
                    print(f"Here's ${round(change,2)} in change.")
                    print(f"Here's is your {question} ☕️. Enjoy!")
                else:
                    more_money = float(MENU[question]['cost']) - sum_coins
                    print("Sorry that's not enough money. Money refunded.")
                    print(f"Please insert ${more_money} more.")
                    
