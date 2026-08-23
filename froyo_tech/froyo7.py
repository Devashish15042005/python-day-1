import pandas as pd
df = pd.read_csv("driverdata.csv")
print(df.head(2))
x = df[['Distance_Feature', 'Speeding_Feature']]
y = df['Pre_Class']
import matplotlib.pyplot as plt
for grp in df['Pre_Class'].unique():
    df1 = x[df['Pre_Class'] == grp]
    plt.scatter(df1['Distance_Feature'], df1['Speeding_Feature'], label=grp)
    plt.xlabel('Distance')
    plt.ylabel('Speed')
    plt.legend()
    plt.show()
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(x, y)
knn.score(x, y)
df['Pre_Class1'] = knn.predict(x)
pd.crosstab(df['Pre_Class'], df['Pre_Class1'], margins=True)