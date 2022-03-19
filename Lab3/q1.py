import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Social_Network_Ads.csv')
plt.hist(
        df['EstimatedSalary'],
        color='blue',
        edgecolor='white',
        bins=4
        )
plt.show()
