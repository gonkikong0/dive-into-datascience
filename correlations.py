import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

hour = pd.read_csv('hour.csv')

# print(hour['casual'].corr(hour['registered']))
# print(hour['temp'].corr(hour['hum'])) #Correlation Coefficient (Pearson Correlation Coefficient )

thenames = ['hr', 'temp', 'windspeed']
cor_matrix = hour[thenames].corr()
print(cor_matrix)