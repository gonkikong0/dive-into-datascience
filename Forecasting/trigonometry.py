
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

plt.plot(x, y)
plt.title('Car sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()  