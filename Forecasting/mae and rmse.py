#Creating functions for rmse and mae >

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


def get_mae(line, actual):
    error = [(x-y)for x,y in zip(line,actual)]
    errorabs = [abs(value) for value in error]
    mae = np.mean(errorabs)
    return(mae)

def get_rmse(line, actual):
    error = [(x-y) for x,y in zip(line,actual)]
    errorsquared = [(value)**2 for value in error]
    rmse = np.sqrt(np.mean(errorsquared))
    return(rmse)