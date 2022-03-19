import pandas as pd

df = pd.read_csv("Data.csv")

sal_class = []

i = 0
while i < 10:
    
    sal = df['Salary'][i]
    
    if sal>70000:
        sal_class.append('class0')
    elif sal>=61000:
        sal_class.append('class1')
    elif sal >= 48000:
        sal_class.append('class2')
    else:
        sal_class.append('')
    
    i += 1

df['Salary_class'] = sal_class

print(df)