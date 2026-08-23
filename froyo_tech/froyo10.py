import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

df=pd.read_csv(r"C:\Users\Lenovo\Desktop\python day 1\froyo_tech\CS11DataSet.csv")
print(df.head(5))

X=df[['ExperienceYears','MonthlyHours','TrainingHours',
      'JobSatisfaction','StressLevel']]
Y=df['PerformanceCategory']

# Correlation
sb.heatmap(df.corr(),annot=True)
plt.show()

# Scatter plot
for grp in df['PerformanceCategory'].unique():
    df1=df[df['PerformanceCategory']==grp]
    plt.scatter(df1['JobSatisfaction'],df1['StressLevel'],label=grp)

plt.xlabel('Job Satisfaction')
plt.ylabel('Stress Level')
plt.legend()
plt.show()

# KNN
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X,Y)

print("Accuracy:",knn.score(X,Y))

df['Performance_Predicted']=knn.predict(X)

print(pd.crosstab(df['PerformanceCategory'],
                  df['Performance_Predicted'],margins=True))

print(classification_report(df['PerformanceCategory'],
                            df['Performance_Predicted']))