import pandas
df = pandas.read_csv("C:\\Users\\55599\\Desktop\\Python Portfolio\\#19_NY_Central_Park_Squirrel_Pandas\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# chosing selected columns
data = df[["Unique Squirrel ID","Primary Fur Color"]]


#finding only grey squirrels
grey_squirrels = data[data["Primary Fur Color"] == "grey"]

# grouping by Fur Color and counting
new_data = data.groupby("Primary Fur Color").count()
# rename the column name
new_data=new_data.rename(columns= {'Unique Squirrel ID': 'Count'})
# save data to new file
new_data.to_csv("C:\\Users\\55599\\Desktop\\Python Portfolio\\#19_NY_Central_Park_Squirrel_Pandas\\Count_of_fur_color.csv")
