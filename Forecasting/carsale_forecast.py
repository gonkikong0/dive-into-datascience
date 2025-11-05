import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

carsales = pd.read_csv('carsales.csv')
carsales.columns = ['month', 'sales']

carsales = carsales.loc[0:107, :].copy()

carsales['period'] = list(range(108))

plt.scatter(carsales['period'], carsales['sales'])
plt.plot(carsales['period'], [81.2 * i + 10250.8 for i in carsales['period']], 'r-', label = 'Regression Line')
plt.plot(carsales['period'], [125 * i + 8000 for i in carsales['period']], 'r--', label = 'Hypothesized Line')
# plt.title('Car sales by Month')
plt.legend(loc= "upper left")
plt.title('Car sales by month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

x = carsales['period'].values.reshape(-1,1)
y = carsales['sales'].values.reshape(-1,1)

saleslist = carsales['sales'].tolist()
regressionline = [81.2 * i + 10250.8 for i in carsales['period']]
hypothesizedline = [125 * i + 8000 for i in carsales['period']]
error1 = [(x-y) for x,y in zip(regressionline, saleslist)]
error2 = [(x-y) for x,y in zip(hypothesizedline, saleslist)]

print(error1)
print(error2)

#Absolute Value
error1abs = [abs(value) for value in error1]
error2abs = [abs(value) for value in error2]

print(np.mean(error1abs))
print(np.mean(error2abs))

#RMS Error

error1squared = [(value)**2 for value in error1]
error2squared = [(value)**2 for value in error2]


print(np.sqrt(np.mean(error1squared)))
print(np.sqrt(np.mean(error2squared)))