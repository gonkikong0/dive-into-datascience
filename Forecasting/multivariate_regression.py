
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


carsales = pd.read_csv('carsales.csv')
carsales.columns = ['month', 'sales']

carsales = carsales.loc[0:107, :].copy()

carsales['period'] = list(range(108))
x = carsales['period'].values.reshape(-1,1)
y = carsales['sales'].values.reshape(-1,1)


carsales['quadratic'] = carsales['period'].apply(lambda x: x**2)
carsales['cubic'] = carsales['period'].apply(lambda x: x**3)

x3 = carsales.loc[:, ['period', 'quadratic', 'cubic']].values.reshape(-1,3)
y = carsales['sales'].values.reshape(-1,1)

regressor = LinearRegression()
regressor.fit(x,y)
regressor_cubic = LinearRegression()
regressor_cubic.fit(x3, y)

plt.scatter(carsales['period'], carsales['sales'])
plt.plot(x, regressor.predict(x), 'r-')
plt.plot(x, regressor_cubic.predict(x3), 'r--')
plt.title('Car sales by Monat')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

print(regressor_cubic.coef_)
print(regressor_cubic.intercept_)
