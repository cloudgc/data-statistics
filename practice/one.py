# encode=utf-8

"""
一维数组
"""
import pandas as pd

stocks = pd.Series([20.1, 100.0, 66.5], index=['tx', 'tobao', 'apple'])

stocks2 = pd.Series([23.1, 95, 88], index=['tx', 'tobao', 'google'])

# stocks average
average = stocks.mean

"""
二维数组
"""

# use numpy
import numpy as np

sdarry = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# different way to get element
print(sdarry[1, 2])
print(sdarry[:, 2])
print(sdarry[2, :])

# get a row or a column mean of data
# axis=1 is row
# axis=0 is column
print(sdarry.mean(), sdarry.mean(axis=1), sdarry.mean(axis=0))

# use pandas

saleLog = {
    'date': ['2018-01-01', '2018-01-02', '2018-01-03'],
    'cardno': ['001', '002', '001'],
    'name': ['vc银翘片', '清热解毒片', '感康'],
    'num': [3, 2, 5],
    'money': [18, 22.1, 61.6],
    'actually': [16.1, 20.3, 52.1]
}

saleDf = pd.DataFrame(saleLog)

from collections import OrderedDict as od

saleLog = {
    'date': ['2018-01-01', '2018-01-02', '2018-01-03'],
    'cardno': ['001', '002', '001'],
    'name': ['vc银翘片', '清热解毒片', '感康'],
    'num': [3, 2, 5],
    'money': [18, 22.1, 61.6],
    'actually': [16.1, 20.3, 52.1]
}

saleOrderDict = od(saleLog)
saleDf = pd.DataFrame(saleOrderDict)

# iloc only accept int type for index
print(saleDf.iloc[0, 1], saleDf[:, 1])

# loc column only accept string for index

# print(saleDf.loc[0, 1]) this is error
print(saleDf.loc[0, 'name'])

# easy way
saleDf.loc[:, 'name'] == saleDf['name']
