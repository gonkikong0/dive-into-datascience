import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mlb = pd.read_csv('mlb.csv')


sample1 = mlb.sample(n = 30, random_state = 8675309)
sample2 = mlb.sample(n = 30, random_state = 1729)

sample3 = [71, 72, 73, 74, 74, 76, 75, 75, 75, 76, 75, 77, 76, 75, 77, 76, 75, 76, 76, 75, 75, 81, 77, 75, 77, 75, 77, 77, 75, 75]


# fig1, ax1 = plt.subplots()
# ax1.boxplot([mlb['height'], sample1['height'], sample2['height'], np.array(sample3)])
# ax1.set_ylabel('Height - Inches')

# plt.title('MLB Player Heights')
# plt.xticks([1, 2, 3,4], ['Full Population', 'Sample 1', 'Sample 2', 'Sample 3'])


print(np.mean(sample1['height']))
print(np.mean(sample2['height']))
print(np.mean(sample3))


alldifferences = []
for i in range(1000):
    newsample1 = mlb.sample(n=30, random_state=i*2)
    newsample2 = mlb.sample(n=30, random_state=i*2+1)
    alldifferences.append(newsample1['height'].mean() - newsample2['height'].mean())

print(alldifferences[0:10])

sns.set()
ax = sns.distplot(alldifferences).set_title("Difference between Sample Means")
plt.xlabel('Difference Between Means - Inches')
plt.ylabel(' Relative Frequency')
plt.show()