import pandas as pd
import matplotlib.pyplot as plt

hour = pd.read_csv('hour.csv')

fig,ax = plt.subplots(figsize =(10,6))
ax.scatter(x = hour['instant'], y = hour['count'])
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Ridership count (by Hour)")

plt.show()

