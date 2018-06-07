import pandas as pd

filepath = './read.xlsx'
xls = pd.ExcelFile(filepath)
salesDf = xls.parse("Sheet1")
print(salesDf.describe())

print(salesDf.head())

print(salesDf.loc[:, 'name':'money'])
search = salesDf.loc[:, 'num'] > 2

print(salesDf.loc[search, :])


print(salesDf.shape)
