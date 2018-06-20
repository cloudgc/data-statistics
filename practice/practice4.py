# -*- coding: UTF-8 -*-
"""
    数据处理

    第一步: 选取子集
    第二步: 列重命名
    第三步：缺失数据处理
    第四步：数据类型转换
    第五步：数据排序
    第六步：异常值处理

"""

import pandas as pd

'''
第一步: 选取子集
'''
cyFile = './data/cy2018.xlsx'
cyXlsx = pd.ExcelFile(cyFile, dtype='object')
# cyXlsx.sheet_names
cyDf = cyXlsx.parse('Sheet1')

cyDf.describe()
cyDf.head()

'''
第二步: 列重命名
'''

newColumsDic = {'购药时间': 'time', '社保卡号': 'certNo', '商品编码': 'saleId',
                '商品名称': 'saleName', '销售数量': 'saleNum', '应收金额': 'chargeM',
                '实收金额': 'taken'}

cyDf.rename(columns=newColumsDic, inplace=True)

'''
第三步：缺失数据处理
    删除缺失或者模型不足
'''

# cyDf.shape
cyDf = cyDf.dropna(subset=['time', 'certNo'], how='any')
# cyDf.shape

'''
第四步：数据类型转换
    删除缺失或者模型不足
'''

cyDf['saleNum'] = cyDf['saleNum'].astype('float')

cytypes = cyDf.dtypes

timeData = cyDf.loc[:, 'time']


def splitTime(originalData):
    timelist = []
    for value in originalData:
        dateStr = value.split(' ')[0]
        timelist.append(dateStr)

    timeClsSer = pd.Series(timelist)
    return timeClsSer


timeSeri = splitTime(timeData)

cyDf.loc[:, 'time'] = timeSeri

cyDf.loc[:, 'time'] = pd.to_datetime(cyDf.loc[:, 'time'], format='%Y-%m-%d', errors='coerce')

cyDf=cyDf.dropna(subset=['time', 'certNo'], how='any')

