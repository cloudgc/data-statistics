# encode=utf-8

"""
一维数组
"""
import pandas as pd
stocks = pd.Series([20.1, 100.0, 66.5], index=['tx', 'tobao', 'apple'])

stocks2 = pd.Series([23.1, 95, 88], index=['tx', 'tobao', 'google'])

# stocks average
average=stocks.mean

