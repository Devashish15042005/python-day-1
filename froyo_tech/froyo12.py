"""
Case Study 13: Predicting Heart Disease Risk using Decision Tree Classification
Target: HeartDiseaseRisk (1 = High-Risk, 0 = Low-Risk)
Features: Age, Cholesterol, BloodPressure, MaxHeartRate, Smoking
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import matplotlib.pyplot as plt

# ---------- 1. Load data ----------
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\python day 1\froyo_tech\CS13DataSet.csv")

features = ["Age", "Cholesterol", "BloodPressure", "MaxHeartRate", "Smoking"]
target = "HeartDiseaseRisk"

X = df[features]
y = df[target]

# ---------- 2. Train/test split ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---------- 3. Train Decision Tree ----------
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,          # tune as needed to avoid overfitting
    random_state=42
)
model.fit(X_train, y_train)

# ---------- 4. Predictions & evaluation (Q2) ----------
y_pred = model.predict(X_test)

print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1-score :", f1_score(y_test, y_pred))
print("\nFull report:\n", classification_report(y_test, y_pred))

# ---------- 5. Feature importance (Q1) ----------
importance = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
print("\nFeature Importance:\n", importance)

# ---------- 6. Visualize the tree ----------
plt.figure(figsize=(20, 10))
plot_tree(
    model,
    feature_names=features,
    class_names=["Low-Risk", "High-Risk"],
    filled=True,
    rounded=True,
    fontsize=8
)
plt.title("Decision Tree - Heart Disease Risk Prediction")
plt.savefig("CS13_decision_tree.png", dpi=200, bbox_inches="tight")
plt.show()

# ---------- 7. Q3: Effect of Cholesterol ----------
print("\nHigh-risk rate by Cholesterol bin:")
print(df.groupby(pd.cut(df["Cholesterol"], bins=5))[target].mean())

# ---------- 8. Q4: Effect of Smoking ----------
print("\nHigh-risk rate by Smoking status:")
print(df.groupby("Smoking")[target].mean())

# ---------- 9. Q5: Highest-risk patient segment ----------
# Combine BloodPressure, MaxHeartRate, Smoking into risk segments
risk_view = df.groupby([
    pd.cut(df["BloodPressure"], bins=3),
    pd.cut(df["MaxHeartRate"], bins=3),
    "Smoking"
])[target].mean().sort_values(ascending=False)
print("\nTop risk segments (BloodPressure x MaxHeartRate x Smoking):\n", risk_view.head(10))