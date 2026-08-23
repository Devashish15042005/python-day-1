import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df=pd.read_csv("diabetes.csv")
print(df.head(4))
df.shape
x=df[['Glucose']]
y=df['Outcome']
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.30)
print(x.shape,X_train.shape,X_test.shape)
lr=LogisticRegression()
lr.fit(X_train,Y_train)
lr.score(X_test,Y_test)
df['Outcome1']=lr.predict(x)
pd.crosstab(df['Outcome'],df['Outcome'],margins=True)
from sklearn.metrics import classification_report

print(classification_report(df['Outcome'],df['Outcome1']))