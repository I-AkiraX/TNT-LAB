import pandas as pd
df=pd.read_csv("data.csv").dropna()
print(df)
print(pd.crosstab(index=df['Country'], columns=df['Purchased'],normalize=True,dropna=True))

print(pd.crosstab(index=df['Country'], columns=df['Purchased'],normalize=True,margins=True,dropna=True))

print(pd.crosstab(index=df['Country'], columns=df['Purchased'],normalize='columns',margins=True,dropna=True))

print(pd.crosstab(index=df['Purchased'], columns=df['Country'],normalize='columns',margins=True,dropna=True))
