import random
#List Comprehension
## new_list = [new item for item in list]

#Numbers
numbers = [1,2,3]
new_numbers = [ i+1 for i in numbers]
#String
name = "Grzegorz"
new_list = [letter for letter in name]
#Range
range_list = range(1,5)
new_list = [i*2 for i in range_list]

#Conditional List Comprehension
## new_list = [new_item for item in list if test]
names = ['Kuba','Grzegorz','Michał']
new_list = [i for i in names if len(i)<5] #challenge: only short names
new_list = [i.upper() for i in names if len(i)>5] #challenge: long names uppercase


#Dictionary Comprehension
## new_dict = {new_key:new_value for item in list}
### new_dict = {new_key:new_value for (key,value) in dict.items()}
#### new_dict = {new_key:new_value for (key,value) in dict.items() if test}


names = ['Kuba','Grzegorz','Michał']

new_dict = {i:random.randint(1,100) for i in names} #assigning random numbers to names
print(new_dict)
### !!!!! IMPORTANT !!!!! jak loopujemy przez dic trzeba dodac dict.items()
#new_dict = {key:value for (key,value) in new_dict.items() if value > 50} # choosing selected names with good score

for (key, value) in new_dict.items():
    print(key)

#Pandas Frame
import pandas
new_dict = {"imie": ['Greg',"Iw"], "wynik": [10,20]}
new_df = pandas.DataFrame(new_dict)
print(new_df)

## Looping through rows
for (index, row) in new_df.iterrows():
    print(index) # pokaze index rzedu
    print(row.imie) # pokaze wszystkie imiona w df
    print(row) # pokaze wszystkie dane z poszczegolnego

# DataFrame comprehension

test = {new_key:new_value for (index,row) in new_df.iterrows()}


########### Stworzenie listy która będzie pobierać dane ze slownika

#TODO 1. Create a dictionary in this format:

df = "C:\\Users\\55599\\Desktop\\Python Portfolio\\#21_NATO_Alphabet_Project\\nato_phonetic_alphabet.csv"
df = pandas.read_csv(df)
# stworzenie slownika
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

text = input("What's the word: ").upper()
# stworzenie listy
nato_alphabet = [new_dict[i] for i in text] # !!!!! BARDZO WAZNE tutaj jest new_dict[i] >>> wziecie ODPOWIEDNIEJ DANEJ ZE SLOWNIKA
print(nato_alphabet)