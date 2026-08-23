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
DATA_PATH = "CS7Dataset.csv"   # <-- place the file in the same folder, or edit this path
 
# --------------------------------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------------------------------
df = pd.read_csv(DATA_PATH)
 
feature_cols = ["ExperienceYears", "TrainingHours", "PerformanceRating", "LeadershipScore", "ProjectsLed"]
target_col = "Promoted"
 
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
# Q3 — ProjectsLed effect
# --------------------------------------------------------------------------
proj_coef = coef_df.loc[coef_df["Variable"] == "ProjectsLed", "Coefficient (standardized)"].values[0]
proj_or = coef_df.loc[coef_df["Variable"] == "ProjectsLed", "Odds Ratio"].values[0]
 
print("\n" + "=" * 70)
print("Q3: Effect of ProjectsLed")
print("=" * 70)
direction = "increases" if proj_coef > 0 else "decreases"
print(f"Coefficient: {proj_coef:.3f}  |  Odds Ratio: {proj_or:.3f}")
print(f"-> A 1-standard-deviation increase in ProjectsLed {direction} "
      f"the odds of promotion by a factor of {proj_or:.2f} "
      f"({(proj_or - 1) * 100:.1f}% change), holding other variables constant.")
 
# --------------------------------------------------------------------------
# Q4 — PerformanceRating effect
# --------------------------------------------------------------------------
perf_coef = coef_df.loc[coef_df["Variable"] == "PerformanceRating", "Coefficient (standardized)"].values[0]
perf_or = coef_df.loc[coef_df["Variable"] == "PerformanceRating", "Odds Ratio"].values[0]
 
print("\n" + "=" * 70)
print("Q4: Effect of PerformanceRating")
print("=" * 70)
direction = "increases" if perf_coef > 0 else "decreases"
print(f"Coefficient: {perf_coef:.3f}  |  Odds Ratio: {perf_or:.3f}")
print(f"-> A 1-standard-deviation increase in PerformanceRating {direction} "
      f"the odds of promotion by a factor of {perf_or:.2f} "
      f"({(perf_or - 1) * 100:.1f}% change), holding other variables constant.")
 
# --------------------------------------------------------------------------
# Q5 — Employees at highest risk of being overlooked (low promotion probability)
#      combining ExperienceYears, TrainingHours, LeadershipScore
# --------------------------------------------------------------------------
df_full_scaled = scaler.transform(X)
df["PredictedProb"] = model.predict_proba(df_full_scaled)[:, 1]
 
df["ExperienceGroup"] = pd.cut(df["ExperienceYears"], bins=[0, 3, 6, 20], labels=["Junior(<=3)", "Mid(4-6)", "Senior(7+)"])
df["TrainingGroup"] = pd.cut(df["TrainingHours"], bins=[0, 25, 38, 100], labels=["Low(<=25)", "Medium(26-38)", "High(39+)"])
df["LeadershipGroup"] = pd.cut(df["LeadershipScore"], bins=[0, 5, 6, 10], labels=["Low(<=5)", "Medium(6)", "High(7+)"])
 
segment_risk = (
    df.groupby(["ExperienceGroup", "TrainingGroup", "LeadershipGroup"], observed=True)["PredictedProb"]
    .agg(["mean", "count"])
    .sort_values("mean", ascending=True)   # ascending -> lowest promotion probability first = most overlooked
)
 
print("\n" + "=" * 70)
print("Q5: Segments at Highest Risk of Being Overlooked for Promotion")
print("=" * 70)
print("(sorted by LOWEST predicted promotion probability first)")
print(segment_risk.head(10).to_string())
 
top_overlooked = segment_risk.iloc[0]
print(f"\nMost overlooked segment: {segment_risk.index[0]} "
      f"-> mean predicted promotion probability = {top_overlooked['mean']:.2%} "
      f"(n={int(top_overlooked['count'])})")