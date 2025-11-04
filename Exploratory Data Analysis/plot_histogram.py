import pandas as pd
import matplotlib.pyplot as plt

hour = pd.read_csv('hour.csv')

fig, ax = plt.subplots(figsize = (10,6))
ax.hist(hour['count'], bins=80)
plt.xlabel("Ridership")
plt.ylabel("Frequency")
plt.title("Ridership Histogram")

plt.show()

