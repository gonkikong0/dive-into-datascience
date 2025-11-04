import pandas as pd

hour = pd.read_csv('hour.csv')

# print(hour['count'].mean()) 
# print(hour['count'].median())
# print(hour['count'].std())    #Summary Statistics
# print(hour['count'].min())
# print(hour['count'].max())

# print(hour.describe()) #Summary Statistics 

# print(hour.loc[2:4,'count']) #Loc() Used to specify a subset [<row>,<column>]



# print(hour.loc[hour['hr'] < 5, 'registered'].mean())
# print(hour.loc[hour['hr'] < 5, 'casual'].mean())

# print(hour.loc[(hour['hr']< 5) & (hour['temp'] < .50), 'count'].mean()) #Analyzing subsets -- (Nighttime Data)
# print(hour.loc[(hour['hr']< 5) & (hour['temp'] > .50), 'count'].mean())  # 0 Represents very cold and 1 represents very warm temperature.

#SEASON --> 1 for winter, 2 for spring, 3 for summer, 4 for fall >

# print(hour.groupby(['season'])['count'].mean())
print(len(hour.groupby(['season', 'holiday'])['count'].mean()))