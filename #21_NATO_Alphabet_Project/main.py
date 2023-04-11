import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = "C:\\Users\\55599\\Desktop\\Python Portfolio\\#21_NATO_Alphabet_Project\\nato_phonetic_alphabet.csv"
df = pandas.read_csv(df)
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(new_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
text = input("What's the word: ").upper()
print(text)

nato_alphabet = [new_dict[i] for i in text]
print(nato_alphabet)

