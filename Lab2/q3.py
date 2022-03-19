import pandas as pd
df=pd.read_csv("data.csv").dropna()
print(df)
print(pd.crosstab(index=df['Country'], columns=df['Purchased'],dropna=True))