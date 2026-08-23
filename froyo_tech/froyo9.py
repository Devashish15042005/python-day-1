import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

df=pd.read_csv(r"C:\Users\Lenovo\Desktop\python day 1\froyo_tech\CS10DataSet.csv")
print(df.head(5))

X=df[['Distance','LoadWeight','AvgSpeed','TrafficIndex','WeatherSeverity']]
Y=df['TripRisk']

# Correlation
sb.heatmap(df.corr(),annot=True)
plt.show()

# Scatter plot
for grp in df['TripRisk'].unique():
    df1=df[df['TripRisk']==grp]
    plt.scatter(df1['TrafficIndex'],df1['WeatherSeverity'],label=grp)

plt.xlabel('Traffic Index')
plt.ylabel('Weather Severity')
plt.legend()
plt.show()

# KNN
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X,Y)

print("Accuracy:",knn.score(X,Y))

df['Risk_Predicted']=knn.predict(X)

print(pd.crosstab(df['TripRisk'],df['Risk_Predicted'],margins=True))

print(classification_report(df['TripRisk'],df['Risk_Predicted']))