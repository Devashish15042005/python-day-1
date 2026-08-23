import pandas as pd
import matplotlib.pyplot as pl
df = pd.read_excel("Employee-Master.xlsx")
print(df.head(2))
sr = df.groupby('Job Grade')['Salary'].sum()
pl.bar(sr.index, sr.values, color='green', label='Total Salary Paid')
pl.xlabel('Job Grade')
pl.ylabel('Total Salary Paid')
pl.title('Job Grade Salary')
pl.legend()
pl.show()
pl.pie(sr.values, labels=sr.index)
pl.show()
def getgrade(salary):
    if salary >3000:
        return 'Grade-3'
    elif salary < 2000:
        return 'Grade-2'
    else:
        return 'Grade-1'
df['Salary Grade'] = df['Salary'].map(getgrade)
df['Salary Grade'] = pd.cut(df['Salary'], bins=[0, 2000, 3000, float('inf')], labels=('Grade-1', 'Grade-2', 'Grade-3'))