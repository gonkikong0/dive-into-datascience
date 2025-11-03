import pandas as pd
import matplotlib.pyplot as plt

hour = pd.read_csv('hour.csv')

hour_first48 = hour.loc[0:48,:]
fig, ax = plt.subplots(figsize =(10,6))
# ax.scatter(x = hour_first48['instant'], y =hour_first48['count'])
# ax.scatter(x = hour_first48['instant'], y =hour_first48['count'], c= 'red', marker='+')
ax.plot(hour_first48['instant'], hour_first48['casual'],c='red', label='casual', linestyle ='-')
ax.plot(hour_first48['instant'], hour_first48['registered'], c='b', label='registered', linestyle='--')
ax.legend()
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Count by Hour - First two days")
plt.show()