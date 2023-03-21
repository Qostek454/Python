#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#Solutions

starting_letter =  open("C:\\Users\\55599\\Desktop\\Python Portfolio\\#18_Mail_Merge_Challenge\\Input\\Letters\\starting_letter.txt", mode = 'r')
invited_names = open("C:\\Users\\55599\\Desktop\\Python Portfolio\\#18_Mail_Merge_Challenge\\Input\\Names\\invited_names.txt", mode = 'r')
text = starting_letter.read()

for name in invited_names.readlines():
    name = name.replace("\n","")
    print(name)
    with open(f"C:\\Users\\55599\\Desktop\\Python Portfolio\\#18_Mail_Merge_Challenge\\Output\\ReadyToSend\\letter_for_{name}.txt",mode = "w") as file:
        text_letter = text.replace("[name]", f"{name}")
        file.write(text_letter)  
    text_letter = text.replace( f"{name}","[name]")   
    
