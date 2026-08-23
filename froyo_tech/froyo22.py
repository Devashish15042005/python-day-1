import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error as mse, mean_absolute_error as mae, r2_score as r2

# ---- Load data ----
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\PYTHON\froyo_tech\CS19Dataset.csv")
X, y = df.iloc[:, :-1], df["Approved_Interest_Rate"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

# ---- Model A: Linear Regression ----
lin = LinearRegression().fit(Xtr, ytr)
p1 = lin.predict(Xte)

# ---- Model B: SVR (scaling mandatory) ----
sx, sy = StandardScaler(), StandardScaler()
svr = SVR().fit(sx.fit_transform(Xtr), sy.fit_transform(ytr.values.reshape(-1, 1)).ravel())
p2 = sy.inverse_transform(svr.predict(sx.transform(Xte)).reshape(-1, 1)).ravel()

print("===== Model Comparison =====")
for name, p in [("Linear Regression", p1), ("SVR", p2)]:
    print(f"{name}: RMSE={mse(yte,p)**0.5:.3f}  MAE={mae(yte,p):.3f}  R2={r2(yte,p):.3f}")

# ===== Q1: Manual calculation with given weights =====
# Intercept=28.0, Credit_Score=-0.025, DTI=+15.0, Inquiries=+0.50
# Applicant: Credit_Score=700, DTI=0.40, Inquiries=2
q1 = 28.0 + (-0.025 * 700) + (15.0 * 0.40) + (0.50 * 2)
print(f"\nQ1 - Predicted Interest Rate: {q1:.2f}%")

# ===== Q2: Metric interpretation =====
# Model A: RMSE=1.8, MAE=0.6 | Model B: RMSE=0.9, MAE=0.7
print("\nQ2 - Model B handles outliers better (its RMSE-MAE gap is smaller,")
print("     meaning fewer/no large errors). Model A's big RMSE-MAE gap means")
print("     it has some large errors hiding behind a low average (MAE).")
print("     Risk committee should prioritize RMSE, since it penalizes large")
print("     underestimation errors much more heavily than MAE does -- and those")
print("     large errors are exactly what cause defaults.")

# ===== Q3: Feature scaling necessity in SVM =====
print("\nQ3 - SVR uses distance/kernel calculations (e.g. RBF), so a feature like")
print("     Annual_Income (25,000-250,000) would completely dominate a feature")
print("     like DTI (0.05-0.60) without scaling, biasing the model. Linear")
print("     Regression instead learns a separate coefficient per feature that")
print("     automatically absorbs each feature's scale, so unscaled features")
print("     don't affect its predictive accuracy (only the coefficient's size).")

# ===== Q4: R2 from SS values =====
ss_tot, ss_res = 1250, 150
q4 = 1 - (ss_res / ss_tot)
print(f"\nQ4 - R2 = 1 - (SS_res/SS_tot) = 1 - (150/1250) = {q4:.2f}")
print(f"     Business meaning: the model explains {q4*100:.0f}% of the variation")
print("     in approved interest rates using the applicant's risk profile --")
print("     only ~12% of the rate differences remain unexplained by the model.")

# ===== Q5: Best algorithm for final consumption =====
print("\nQ5 - Linear Regression is the better choice here: higher R2, lower")
print("     RMSE/MAE on this dataset, and it's interpretable (clear coefficients),")
print("     which matters for banking/regulatory explainability of loan pricing.")