import pandas as pd
df = pd.read_csv(r'C:\Users\Lenovo\Desktop\PYTHON\froyo_tech\driverdata.csv')
x = df[['Distance_Feature', 'Speeding_Feature']]
from sklearn.cluster import KMeans
n=2
km= KMeans(n_clusters=n)
km.fit(x)
df['Grp'] = km.predict(x)
ar= km.cluster_centers_
print(ar)
import matplotlib.pyplot as plt
for a in df['Grp'].unique():
    df1 = df[df['Grp'] == a]
    plt.scatter(df1['Distance_Feature'], df1['Speeding_Feature'], label=a)
    plt.scatter(ar[a,0], ar[a,1], marker='*', color='black', s=200)
plt.legend()
plt.xlabel('Distance')
plt.ylabel('Speeding')
plt.title('Driver Clustering')
plt.show()