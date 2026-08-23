import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)
 
RANDOM_STATE = 42
DATA_PATH = "CS8Dataset.csv"   # <-- place the file in the same folder, or edit this path
 
# --------------------------------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------------------------------
df = pd.read_csv(DATA_PATH)
 
feature_cols = ["Income", "LoanAmount", "CreditScore", "LatePayments", "UtilizationRate"]
target_col = "Default"
 
df = df.dropna(subset=feature_cols + [target_col])   # basic cleaning
 
X = df[feature_cols]
y = df[target_col]
 
# --------------------------------------------------------------------------
# 2. TRAIN / TEST SPLIT + SCALING
# --------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=RANDOM_STATE, stratify=y
)
 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
 
# --------------------------------------------------------------------------
# 3. FIT LOGISTIC REGRESSION
# --------------------------------------------------------------------------
model = LogisticRegression(random_state=RANDOM_STATE, max_iter=1000)
model.fit(X_train_scaled, y_train)
 
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]
 
# --------------------------------------------------------------------------
# Q1 — Strongest predictor (standardized coefficients -> comparable magnitude)
# --------------------------------------------------------------------------
coef_df = pd.DataFrame({
    "Variable": feature_cols,
    "Coefficient (standardized)": model.coef_[0],
    "Odds Ratio": np.exp(model.coef_[0])
}).sort_values(by="Coefficient (standardized)", key=abs, ascending=False)
 
print("=" * 70)
print("Q1: Logistic Regression Coefficients (standardized -> comparable scale)")
print("=" * 70)
print(coef_df.to_string(index=False))
print(f"\nStrongest predictor: {coef_df.iloc[0]['Variable']} "
      f"(|coef| = {abs(coef_df.iloc[0]['Coefficient (standardized)']):.3f})")
 
# --------------------------------------------------------------------------
# Q2 — Model performance
# --------------------------------------------------------------------------
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_proba)
cm = confusion_matrix(y_test, y_pred)
 
print("\n" + "=" * 70)
print("Q2: Model Performance")
print("=" * 70)
print(f"Accuracy : {acc:.3f}")
print(f"Precision: {prec:.3f}")
print(f"Recall   : {rec:.3f}")
print(f"F1-score : {f1:.3f}")
print(f"ROC-AUC  : {auc:.3f}")
print("\nConfusion Matrix [[TN, FP], [FN, TP]]:")
print(cm)
print("\nFull classification report:")
print(classification_report(y_test, y_pred))
 
# --------------------------------------------------------------------------
# Q3 — UtilizationRate effect
# --------------------------------------------------------------------------
util_coef = coef_df.loc[coef_df["Variable"] == "UtilizationRate", "Coefficient (standardized)"].values[0]
util_or = coef_df.loc[coef_df["Variable"] == "UtilizationRate", "Odds Ratio"].values[0]
 
print("\n" + "=" * 70)
print("Q3: Effect of UtilizationRate")
print("=" * 70)
direction = "increases" if util_coef > 0 else "decreases"
print(f"Coefficient: {util_coef:.3f}  |  Odds Ratio: {util_or:.3f}")
print(f"-> A 1-standard-deviation increase in UtilizationRate {direction} "
      f"the odds of default by a factor of {util_or:.2f} "
      f"({(util_or - 1) * 100:.1f}% change), holding other variables constant.")
 
# --------------------------------------------------------------------------
# Q4 — LatePayments effect
# --------------------------------------------------------------------------
late_coef = coef_df.loc[coef_df["Variable"] == "LatePayments", "Coefficient (standardized)"].values[0]
late_or = coef_df.loc[coef_df["Variable"] == "LatePayments", "Odds Ratio"].values[0]
 
print("\n" + "=" * 70)
print("Q4: Effect of LatePayments")
print("=" * 70)
direction = "increases" if late_coef > 0 else "decreases"
print(f"Coefficient: {late_coef:.3f}  |  Odds Ratio: {late_or:.3f}")
print(f"-> A 1-standard-deviation increase in LatePayments {direction} "
      f"the odds of default by a factor of {late_or:.2f} "
      f"({(late_or - 1) * 100:.1f}% change), holding other variables constant.")
 
# --------------------------------------------------------------------------
# Q5 — Highest-risk customer segment (CreditScore, LoanAmount, LatePayments)
# --------------------------------------------------------------------------
df_full_scaled = scaler.transform(X)
df["PredictedProb"] = model.predict_proba(df_full_scaled)[:, 1]
 
df["CreditScoreGroup"] = pd.cut(df["CreditScore"], bins=[0, 650, 720, 900], labels=["Low(<=650)", "Medium(651-720)", "High(721+)"])
df["LoanAmountGroup"] = pd.cut(df["LoanAmount"], bins=[0, 3, 6, 20], labels=["Small(<=3)", "Medium(4-6)", "Large(7+)"])
df["LatePaymentsGroup"] = pd.cut(df["LatePayments"], bins=[-1, 0, 2, 20], labels=["None(0)", "Few(1-2)", "Many(3+)"])
 
segment_risk = (
    df.groupby(["CreditScoreGroup", "LoanAmountGroup", "LatePaymentsGroup"], observed=True)["PredictedProb"]
    .agg(["mean", "count"])
    .sort_values("mean", ascending=False)
)
 
print("\n" + "=" * 70)
print("Q5: Risk Segmentation by CreditScore / LoanAmount / LatePayments")
print("=" * 70)
print(segment_risk.head(10).to_string())
 
top_segment = segment_risk.iloc[0]
print(f"\nHighest-risk customer segment: {segment_risk.index[0]} "
      f"-> mean predicted default probability = {top_segment['mean']:.2%} "
      f"(n={int(top_segment['count'])})")