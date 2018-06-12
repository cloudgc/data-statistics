import pandas as pd

filepath = './read.xlsx'
xls = pd.ExcelFile(filepath)
salesDf = xls.parse("Sheet1", dtype='object')
print(salesDf.describe())

print(salesDf.head())

print(salesDf.loc[:, 'name':'money'])
search = salesDf.loc[:, 'num'] > 2

print(salesDf.loc[search, :])

print(salesDf.shape)

cy2016 = './cy2016.xlsx'

cyexcel = pd.ExcelFile(cy2016, dtype='object')

cyDf = cyexcel.parse("Sheet1", dtype='object')

print(cyDf.describe())

print(cyDf.head())

cy_num = cyDf.loc[:, '销售数量']

print(cyDf.shape)

'''
    first step 第一步 选择子集
'''
# choose sublist
sub_list = cyDf.loc[0:4, '购药时间':'销售数量']

colNewDict = {'购药时间': 'time'}
'''
inplace False 新列
'''
cyDf.rename(columns=colNewDict, inplace=True)

cyDf.dropna(subset=['time', '社保卡号'], how='any')
