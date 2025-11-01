import pandas as pd

hour = pd.read_csv('hour.csv')

# print(hour['count'].mean()) 
# print(hour['count'].median())
# print(hour['count'].std())
# print(hour['count'].min())
# print(hour['count'].max())

print(hour.describe())