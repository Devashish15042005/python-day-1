import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score

df = pd.read_csv(r"C:\Users\Lenovo\Desktop\PYTHON\froyo_tech\CS20Dataset.csv")
X, y = df.iloc[:, :-1], df["Default_Status"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

sx = StandardScaler()
model = LogisticRegression().fit(sx.fit_transform(Xtr), ytr)
pred = model.predict(sx.transform(Xte))

tn, fp, fn, tp = confusion_matrix(yte, pred).ravel()
precision = precision_score(yte, pred)
recall = recall_score(yte, pred)

print(f"Confusion Matrix -> TN={tn} FP={fp} FN={fn} TP={tp}")
print(f"Accuracy={accuracy_score(yte, pred):.3f}  Precision={precision:.3f}  Recall={recall:.3f}")

# Q1: Financial cost (FN=$10,000, FP=$1,000)
cost = fn * 10000 + fp * 1000
print(f"\nQ1 - Precision={precision:.3f}, Recall={recall:.3f}")
print(f"Q1 - Total Financial Cost = ({fn} FN x $10,000) + ({fp} FP x $1,000) = ${cost:,}")

# ===== Q2: Probability threshold tuning =====
print("\nQ2 - FN costs 10x more than FP ($10,000 vs $1,000), so lower the")
print("     threshold below 0.5 (e.g. 0.2-0.3) to flag more applicants as risky.")
print("     This raises Recall (fewer missed defaulters) at the cost of Precision")
print("     (more good applicants rejected) -- an acceptable trade-off here.")

# ===== Q3: Logistic Regression log-odds derivation =====
print("\nQ3 - p = 1/(1+e^-(b0+b1x1+...+bnxn))  =>  p/(1-p) = e^(b0+b1x1+...+bnxn)")
print("     Taking log of both sides: ln(p/(1-p)) = b0 + b1x1 + ... + bnxn")
print("     i.e. the log-odds (logit) equals the linear combination of features.")

# ===== Q4: Naive Bayes assumption failure =====
print("\nQ4 - Naive Bayes assumes features are conditionally independent given the")
print("     class. In credit risk this fails: Revolving_Util_Rate and DTI are")
print("     correlated, and Inquiries_Last_6Mo correlates with Past_Delinquencies.")
print("     Treating correlated features as independent double-counts evidence,")
print("     skewing probability estimates.")

# ===== Q5: Best algorithm for final consumption =====
print(f"\nQ5 - Logistic Regression is the best choice: Precision={precision:.3f},")
print(f"     Recall={recall:.3f} (defaulters rarely missed), coefficients are")
print("     interpretable for regulators, and Naive Bayes' independence")
print("     assumption is violated here, making it less reliable.")