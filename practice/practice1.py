# encode=utf-8

"""
一维数组
"""
import numpy as np

ndarry = np.array([[35, 20, 66], [23, 67, 89], [13, 244, 67]], np.int32)

print(ndarry.shape, ndarry.size)
print(ndarry.dtype)
print(ndarry[1:2, 1:2])



import pandas as pd

stocks = pd.Series([20.1, 100.0, 66.5], index=['tx', 'tobao', 'apple'])

stocks2 = pd.Series([23.1, 95, 88], index=['tx', 'tobao', 'google'])

# stocks average
average = stocks.mean