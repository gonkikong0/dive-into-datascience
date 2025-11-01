import pandas as pd

hour = pd.read_csv('hour.csv')

# print(hour['count'].mean()) 
# print(hour['count'].median())
# print(hour['count'].std())    #Summary Statistics
# print(hour['count'].min())
# print(hour['count'].max())

# print(hour.describe()) #Summary Statistics 

# print(hour.loc[2:4,'count']) #Loc() Used to specify a subset [<row>,<column>]

print(hour.loc[hour['hr'] < 5, 'registered'].mean())
print(hour.loc[hour['hr'] < 5, 'casual'].mean())