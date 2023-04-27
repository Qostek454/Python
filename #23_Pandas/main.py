# # Pandas Documentation
# #https://pandas.pydata.org/docs/


# # USING PANDAS LIBRARY
# # sometimes before using in VSC type pip install pandas in Terminal
# import pandas as pd


# # reading csv file with pandas library
# df = pandas.read_csv("C:\\Users\\55599\\Desktop\\Python Portfolio\\Pandas\\data.csv")
# print(df) #reading all data
# print(type(df)) #checking the type of the file
# #Series in equal to data in 1 column (it's a dimension)

# # reading data - chosen column
# print(df['temp'])
# print(df.temp)

# # reading row
# print(df[df.day == "Monday"])
# print(df[df.temp == max(df.temp)])

# # reading data from a row

# monday = df[df.day == "Monday"]
# print(monday.condition) # reading condition from row Monday

# # using Series functions mean(avg) and max - simple calcucation on series
# print(df['temp'].mean())
# print(df['temp'].max())


# #Create DataFram
# #data_dict = some data in dictionary format
#  new_ data = pandas.DataFrame(data_dict)

# # Saving data to CSV file
# new_data.to_csv("name of the file.csv")

# #readinf all columns names
# df.columns.values.tolist()

# # grouping by Fur Color and counting
# new_data = df.groupby("Primary Fur Color").count()
# # rename the column name
# new_data=df.rename(columns= {'Unique Squirrel ID': 'Count'})

# #filtering data by selected value in a column
# grey_squirrels = data[data["Primary Fur Color"] == "grey"]

##Pivoting data
import pandas as pd
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
test_df

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
pivoted_df
pivoted_df = test_df.pivot(index='Actor', columns='Age', values='Power')
pivoted_df

## DEaling with NaN Values

pivoted_df.fillna(0, inplace=True) # 0 >> zamiana NaN na 0 >> tutaj można wpisać na co się chce zamienić
# inplace = True >> oznacza że nadpisuje tabele inaczej trzeba byłoby to zrobić tak
#pivoted_df = pivoted_df.fillna(0) 

# Checking NA values
pivoted_df.isna().values.any() # >> uzywają values.any() dostaniemy jedna odpowiedz T lub F
# uzywajac tylko pivoted_df.isna() wyswietli się cała tabale i kazda wartość bedzie zawierac
# T lub F

# Sprawdzanie ile jest unikatowych wartosci w bazie danych

df.nunique()

# sprawdzanie ile jest wystapien per dana kolumna

## 1 
df.groupby("is_trans").count()

## 2
df.is_trans.value_counts()



## Matplotlib.pyplot library
import matplotlib.pyplot as plt

plt.plot(pivoted_df.index, pivoted_df.Old) # x >> nie podaje się nazwy kolumny a po prostu .index
# y >> podaje się nazwe kolumn


## Styling the chart

plt.figure(figsize=(15,5)) # zmiana wielkosci chartu
plt.xlabel("x-label") # x line title
plt.ylabel("y-label") # y line title
plt.ylim(0,25000) # przedziałka osi y
plt.plot(reshaped_df.index, reshaped_df['java'],color = "red") # pierwsza miara na charcie koloru red
plt.plot(reshaped_df.index, reshaped_df['python'],color = "blue") # druga miara na charcie koloru blue

### pokazanie wszystkich miar na jednym charcie - szybki sposob

plt.figure(figsize=(16,10))
plt.ylim(0,35500)
for i in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[i],
             linewidth = 2, label=reshaped_df[i].name) ## dodanie legendy to trzeba tutaj dodac label + poniżej plt.legend

plt.legend(fontsize=10)


