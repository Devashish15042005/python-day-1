import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

df=pd.read_csv(r"C:\Users\Lenovo\Desktop\python day 1\froyo_tech\CS12DataSet.csv")
print(df.head(5))

X=df[['Income','LoanAmount','CreditScore',
      'LatePayments','UtilizationRate']]
Y=df['CreditRiskCategory']

# Correlation
sb.heatmap(df.corr(),annot=True)
plt.show()

# Scatter plot
for grp in df['CreditRiskCategory'].unique():
    df1=df[df['CreditRiskCategory']==grp]
    plt.scatter(df1['CreditScore'],df1['UtilizationRate'],label=grp)

plt.xlabel('Credit Score')
plt.ylabel('Utilization Rate')
plt.legend()
plt.show()

# KNN
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X,Y)

print("Accuracy:",knn.score(X,Y))

df['Risk_Predicted']=knn.predict(X)

print(pd.crosstab(df['CreditRiskCategory'],
                  df['Risk_Predicted'],margins=True))

print(classification_report(df['CreditRiskCategory'],
                            df['Risk_Predicted']))