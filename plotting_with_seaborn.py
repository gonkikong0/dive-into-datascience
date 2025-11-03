import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

hour = pd.read_csv('hour.csv')
print(hour.head(10))

fig,ax = plt.subplots(figsize = (10,6))
sns.boxplot(x='hr', y='registered', data=hour)
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Counts by Hour")
plt.show()