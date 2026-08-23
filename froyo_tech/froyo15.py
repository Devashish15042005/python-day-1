import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

df = pd.read_csv(r"C:\Users\Lenovo\Desktop\PYTHON\froyo_tech\CS15DataSet.csv")

X = df.drop("InfectionStatus", axis=1)
y = df["InfectionStatus"]

# Q1: correlation heatmap
plt.figure(figsize=(6,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.close()

print("Correlation with InfectionStatus:\n", df.corr()["InfectionStatus"].sort_values(ascending=False))

# Q2: train Naive Bayes, evaluate
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nAccuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1-score :", f1_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Q3: Temperature distribution by class
plt.figure(figsize=(5,4))
sns.boxplot(x="InfectionStatus", y="Temperature", data=df)
plt.title("Temperature by Infection Status")
plt.tight_layout()
plt.savefig("temp_boxplot.png")
plt.show()
plt.close()

print("\nMean Temperature (Infected):", df[df.InfectionStatus==1]["Temperature"].mean())
print("Mean Temperature (Not Infected):", df[df.InfectionStatus==0]["Temperature"].mean())

# Q4: WBC count - Naive Bayes learned class-wise mean/std
print("\nGaussianNB learned means (per feature, per class):")
print(pd.DataFrame(model.theta_, columns=X.columns, index=["Not Infected", "Infected"]))

# Q5: Risk segment - high cough + fatigue + temperature
high_risk = df[(df.CoughSeverity >= 7) & (df.FatigueLevel >= 7) & (df.Temperature >= 101)]
print("\nHigh Cough+Fatigue+Temp segment size:", len(high_risk))
print("Infection rate in this segment:", high_risk["InfectionStatus"].mean())
print("Overall infection rate:", df["InfectionStatus"].mean())
