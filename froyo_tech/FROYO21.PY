"""
Case Study 17: Predicting Patient Recovery Time Using SVR
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("CS17DataSet.csv")

FEATURES = ["Age", "InjurySeverity", "PhysiotherapyHours", "MobilityScore", "PainLevel"]
TARGET = "RecoveryTime"
X, y = df[FEATURES], df[TARGET]

# Train/test split + scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler_X, scaler_y = StandardScaler(), StandardScaler()
X_train_s = scaler_X.fit_transform(X_train)
X_test_s = scaler_X.transform(X_test)
y_train_s = scaler_y.fit_transform(y_train.values.reshape(-1, 1)).ravel()

# Train SVR
model = SVR(kernel="rbf", C=100, gamma="scale", epsilon=0.5)
model.fit(X_train_s, y_train_s)
y_pred = scaler_y.inverse_transform(model.predict(X_test_s).reshape(-1, 1)).ravel()

# Metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"MAE: {mae:.2f} | RMSE: {rmse:.2f} | R2: {r2:.3f}")

# Correlation with target (for bar chart)
corr = df.corr()[TARGET].drop(TARGET).sort_values()
print("\nCorrelation with RecoveryTime:\n", corr)

# --- Bar chart: correlation of each feature with RecoveryTime ---
plt.figure(figsize=(7, 5))
sns.barplot(x=corr.values, y=corr.index, hue=corr.index, palette="viridis", legend=False)
plt.title("Feature Correlation with Recovery Time")
plt.xlabel("Correlation")
plt.tight_layout()
plt.savefig("bar_correlation.png", dpi=150)
plt.close()

# --- Scatter plot: Actual vs Predicted ---
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, color="teal", edgecolor="k", s=70)
lims = [y_test.min() - 2, y_test.max() + 2]
plt.plot(lims, lims, "r--", label="Perfect Prediction")
plt.xlabel("Actual Recovery Time (days)")
plt.ylabel("Predicted Recovery Time (days)")
plt.title("Actual vs Predicted Recovery Time (SVR)")
plt.legend()
plt.tight_layout()
plt.savefig("scatter_actual_vs_predicted.png", dpi=150)
plt.close()

print("\nPlots saved: bar_correlation.png, scatter_actual_vs_predicted.png")