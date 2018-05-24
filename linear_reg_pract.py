import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = "EzAELjGNysBk6Nmf5Zn4"

df = quandl.get("WSE/PLAY")

df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
df['hl_pct'] = (df['High'] - df['Close']) / df['Close'] * 100
df['pct_change'] = (df['Close'] - df['Open']) / df['Open'] * 100
df = df[['Close', 'hl_pct', 'pct_change', 'Volume']]

forecast_col = 'Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.1*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

X = preprocessing.scale(X)

X = X[:-forecast_out+1]
df.dropna(inplace=True)
y = np.array(df['label'])

print(len(X), len(y))

print(df.head())
