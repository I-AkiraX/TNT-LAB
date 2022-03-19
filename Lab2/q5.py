import pandas as pd
df=pd.read_csv("data.csv").dropna()
print(df)
print(df.corr(method='pearson'))
