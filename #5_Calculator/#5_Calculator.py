# Calculations  - functions

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# creating dictionary of calculations
dic_calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,   
}

def calculator():
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))

    # printing all symbols
    for i in dic_calculations:
        print(i)

    # picking symbol by user    
        
    symbol = input("Pick an operation from the line above: ")
    answer1 = dic_calculations[symbol](num1,num2)
        
    # printing solution
    print(f"{num1} {symbol} {num2} = {answer1}")

    # continue with calculating

    finish = ''

    while finish != 'n':
        finish = input(f"Type 'y' to continue calculating with {answer1}, or type 'n' to exit.: ")
        if finish == 'n':
            calculator() # recursion function - the calculator restarts
        else: 
            symbol = input("Pick an operation from the line above: ")
            num3 = float(input("What's another number?: "))
            answer2 = dic_calculations[symbol](answer1,num3)
            print(f"{answer1} {symbol} {num3} = {answer2}")
            answer1 = answer2
            
calculator()
