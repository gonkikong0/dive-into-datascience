import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

hour = pd.read_csv('hour.csv')

# print(hour['casual'].corr(hour['registered']))
# print(hour['temp'].corr(hour['hum'])) #Correlation Coefficient (Pearson Correlation Coefficient )

thenames = ['hr', 'temp', 'windspeed']
cor_matrix = hour[thenames].corr()

#HEATMAP for Correlations

plt.figure(figsize = (14,10))
corr = hour[thenames].corr()
sns.heatmap(corr, annot= True, cmap = 'coolwarm',
            fmt = ".3f",
            xticklabels = thenames,
            yticklabels = thenames)
# plt.show()

#HEATMAP for other variables

df_hm = hour.pivot_table(index = 'hr', columns = 'weekday', values ='count')
#Drawing a heatmap

plt.figure(figsize = (20,10)) #To resize
sns.heatmap(df_hm, fmt= "d", cmap = 'coolwarm', linewidths = .5, vmin = 0)
plt.show()