import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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

