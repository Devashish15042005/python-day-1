import pandas as pd
ls = [2, 4, 10, 12, 3, 20, 30, 11, 25]
df = pd.DataFrame({'val':ls})
x = df[['val']]
from sklearn.cluster import KMeans
km = KMeans(n_clusters=2)
km.fit(x)
print(km.cluster_centers_)
df['Grp'] = km.predict(x)
print('first group',df[df['Grp']==0]['val'].values)
print('second group',df[df['Grp']==1]['val'].values)