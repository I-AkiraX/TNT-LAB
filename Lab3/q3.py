import pandas as pd

df = pd.read_csv('Data.csv')

print('Before removing NA Values:', df.shape)

df.dropna(axis=0, inplace=True)

print('After removing NA Values:', df.shape)
