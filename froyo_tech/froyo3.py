#CS5 - Logistic Regression Analysis for Readmission Prediction
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
DATA_PATH = "CS5Dataset.csv"   # <-- place the file in the same folder, or edit this path
 
# --------------------------------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------------------------------
df = pd.read_csv(DATA_PATH)
 
feature_cols = ["Age", "BMI", "HbA1c", "Comorbidities", "DaysInHospital"]
target_col = "Readmitted"
 
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
# Q3 — Comorbidities effect
# --------------------------------------------------------------------------
comorb_coef = coef_df.loc[coef_df["Variable"] == "Comorbidities", "Coefficient (standardized)"].values[0]
comorb_or = coef_df.loc[coef_df["Variable"] == "Comorbidities", "Odds Ratio"].values[0]
 
print("\n" + "=" * 70)
print("Q3: Effect of Comorbidities")
print("=" * 70)
direction = "increases" if comorb_coef > 0 else "decreases"
print(f"Coefficient: {comorb_coef:.3f}  |  Odds Ratio: {comorb_or:.3f}")
print(f"-> A 1-standard-deviation increase in Comorbidities {direction} "
      f"the odds of readmission by a factor of {comorb_or:.2f} "
      f"({(comorb_or - 1) * 100:.1f}% change), holding other variables constant.")
 
# --------------------------------------------------------------------------
# Q4 — DaysInHospital effect
# --------------------------------------------------------------------------
days_coef = coef_df.loc[coef_df["Variable"] == "DaysInHospital", "Coefficient (standardized)"].values[0]
days_or = coef_df.loc[coef_df["Variable"] == "DaysInHospital", "Odds Ratio"].values[0]
 
print("\n" + "=" * 70)
print("Q4: Effect of DaysInHospital")
print("=" * 70)
direction = "increases" if days_coef > 0 else "decreases"
print(f"Coefficient: {days_coef:.3f}  |  Odds Ratio: {days_or:.3f}")
print(f"-> A 1-standard-deviation increase in length of stay {direction} "
      f"the odds of readmission by a factor of {days_or:.2f} "
      f"({(days_or - 1) * 100:.1f}% change), holding other variables constant.")
 
# --------------------------------------------------------------------------
# Q5 — Highest-risk segment (Age, HbA1c, Comorbidities)
# --------------------------------------------------------------------------
df_full_scaled = scaler.transform(X)
df["PredictedProb"] = model.predict_proba(df_full_scaled)[:, 1]
 
# bucket into segments for interpretability
df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 40, 60, 120], labels=["<40", "40-60", "60+"])
df["HbA1cGroup"] = pd.cut(df["HbA1c"], bins=[0, 6.5, 8.0, 20], labels=["Normal(<6.5)", "Elevated(6.5-8)", "High(>8)"])
df["ComorbGroup"] = pd.cut(df["Comorbidities"], bins=[-1, 1, 3, 20], labels=["0-1", "2-3", "4+"])
 
segment_risk = (
    df.groupby(["AgeGroup", "HbA1cGroup", "ComorbGroup"], observed=True)["PredictedProb"]
    .agg(["mean", "count"])
    .sort_values("mean", ascending=False)
)
 
print("\n" + "=" * 70)
print("Q5: Risk Stratification by Age / HbA1c / Comorbidities")
print("=" * 70)
print(segment_risk.head(10).to_string())
 
top_segment = segment_risk.iloc[0]
print(f"\nHighest-risk segment: {segment_risk.index[0]} "
      f"-> mean predicted readmission probability = {top_segment['mean']:.2%} "
      f"(n={int(top_segment['count'])})")