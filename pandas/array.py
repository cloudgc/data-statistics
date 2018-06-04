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
