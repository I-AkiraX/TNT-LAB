import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Social_Network_Ads.csv')

print('A')
ax = sns.distplot(
        df.EstimatedSalary,
        bins=5
        )
plt.show()

print('B')
ax = sns.distplot(
        df.EstimatedSalary,
        bins=10,
        kde=False
        )
plt.show()
