import pandas as pd

stocks = pd.Series([20.1, 100.0, 66.5], index=["apple", "tobao", "tx"])

stocks.describe()

stocks.iloc[0]

stocks.loc['tobao']
