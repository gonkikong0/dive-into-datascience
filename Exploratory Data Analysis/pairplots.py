import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

hour = pd.read_csv('hour.csv')

thevariables = ['hr', 'temp', 'windspeed']
hour_first100 = hour.loc[0:100, thevariables]
sns.pairplot(hour_first100, corner = True)
plt.show()