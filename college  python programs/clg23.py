import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
url = "http://froyotechnologies.in/TempResources/CaseStudy-2-Sales-Marks.xlsx"
df = pd.read_excel(url)
print(df.head())
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='Month', y='CategoryA', marker='o', label='Category A')
sns.lineplot(data=df, x='Month', y='CategoryB', marker='o', label='Category B')
sns.lineplot(data=df, x='Month', y='CategoryC', marker='o', label='Category C')
plt.title("Monthly Sales Trend of All Three Categories")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
