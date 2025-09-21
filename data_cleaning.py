
import numpy as np
import pandas as pd

df = pd.read_csv("/content/btc_1h.csv", parse_dates = True)

df = df.rename(columns={'Timestamp': 'Date'})

df = df.set_index('Date')
df

print("DataSet Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nCoulumn Data Types:")
print(df.dtypes)
print("\nSummary Statistics:")
print(df.describe())

print(df.isnull().sum())

df.fillna(method = 'ffill', inplace = True)

df.dropna(inplace = True)

df = df[~df.index.duplicated(keep = 'first')]

df['Low'] = df['Low'].clip(lower = 1)

df = df.sort_index()

df.to_csv("btc_1h_cleaned.csv")
