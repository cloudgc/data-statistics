import pandas as pd

stocks = pd.Series([20.1, 100.0, 66.5], index=['tx', 'tobao', 'apple'])

print(stocks.describe())
print(stocks.iloc[0])
print(stocks.loc['tobao'])

print(stocks.mean)

stocks2 = pd.Series([23.1, 95, 88], index=['tx', 'tobao', 'google'])

# stocks3 = pd.Series([25, 96, 61.2], index=["apple", "tobao", "tx"])
dif = stocks + stocks2
print(dif)
print(dif.dropna())

dif = stocks2.add(stocks, fill_value=0)
print(dif)

saleLog = {
    'date': ['2018-01-01', '2018-01-02', '2018-01-03'],
    'cardno': ['001', '002', '001'],
    'name': ['vc银翘片', '清热解毒片', '感康'],
    'num': [3, 2, 5],
    'money': [18, 22.1, 61.6],
    'actually': [16.1, 20.3, 52.1]
}

saleDf = pd.DataFrame(saleLog)

print(saleDf)

from collections import OrderedDict

saleOrderDict = OrderedDict(saleLog)
print(saleOrderDict)

saleOrderDf = pd.DataFrame(saleOrderDict)
print(saleOrderDf)

print(saleOrderDf.mean())

print(saleOrderDf.iloc[0, 1])

print(saleOrderDf.iloc[0, :])
print(saleOrderDf.iloc[:, 0])

print(saleOrderDf.loc[0, 'name'])
print(saleOrderDf.loc[0, :])
print(saleOrderDf.loc[:, 'name'])

print(saleOrderDf['name'])
print(saleOrderDf[['name', 'actually']])
print(saleOrderDf.loc[:, 'date': 'actually'])

qrySer = saleOrderDf.loc[:, 'num'] > 2
print(qrySer)

print(saleOrderDf.loc[qrySer, :])

pd.read
