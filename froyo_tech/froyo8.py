# case study 9 sollution

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

df=pd.read_csv(r"C:\Users\Lenovo\Desktop\python day 1\froyo_tech\CS9DataSet.csv")
print(df.head(5))

X=df[['Age','BMI','GlucoseLevel','BloodPressure','PhysicalActivity']]
Y=df['DiabetesRisk']

# Correlation
sb.heatmap(df.corr(),annot=True)
plt.show()

# Scatter plot
for grp in df['DiabetesRisk'].unique():
    df1=df[df['DiabetesRisk']==grp]
    plt.scatter(df1['GlucoseLevel'],df1['BMI'],label=grp)

plt.xlabel('Glucose Level')
plt.ylabel('BMI')
plt.legend()
plt.show()

# KNN
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X,Y)

print("Accuracy:",knn.score(X,Y))

df['Risk_Predicted']=knn.predict(X)

print(pd.crosstab(df['DiabetesRisk'],df['Risk_Predicted'],margins=True))

# Classification report
print(classification_report(df['DiabetesRisk'],df['Risk_Predicted']))