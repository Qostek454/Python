#Password Generator Project

# libraries
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []
password = ""

# Intro
print("Welcome to the PyPassword Generator!")


# choosing #of letters/symbols/numbers
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - create password in order 1.Letters 2.Symbols 3.Numbers

for i in range(1, nr_letters + 1):
   password += random.choice(letters)

for i in range(1, nr_symbols + 1):
   password += random.choice(symbols)

for i in range(1, nr_numbers + 1):
   password += random.choice(numbers)

print("Your easy level password: ",password)

#Hard Level - shuffle order of letters/symbols/numbers

for i in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for i in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for i in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# shuffling password_list
random.shuffle(password_list)

# Creating password
password = ""
for i in password_list:
  password += i

# Output
print(f"Your password is: {password}")