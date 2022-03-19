import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Social_Network_Ads.csv").dropna()
print(df.head())
df.plot.scatter(x='Age',y='EstimatedSalary')
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
