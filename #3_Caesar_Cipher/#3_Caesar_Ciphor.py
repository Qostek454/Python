alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
             'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 
             'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Creating function to encode/decode message. 

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      # if there is decode direction, user will be moving back through alphabet 
      shift_amount *= -1
  # Looping through input message (letter by letter)
  for i in start_text:
    # cheking if there is a space in message - if yes add space
    if i != " ":
    # knowing position of a letter in alphabet / adding shift number to know ciphered letter / knowing the "new" letter
        position = alphabet.index(i)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else: 
        end_text += " "
        continue
  print(f"Here's the {direction}d result: {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)