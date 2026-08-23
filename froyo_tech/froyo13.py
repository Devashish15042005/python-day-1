"""
Case Study 14: Predicting Shipment Delay using Decision Tree Classification
Target: ShipmentDelay (1 = Delayed, 0 = On-Time)
Features: Distance, LoadWeight, AvgSpeed, TrafficIndex, WeatherSeverity
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import matplotlib.pyplot as plt

# ---------- 1. Load data ----------
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\python day 1\froyo_tech\CS14DataSet.csv")

features = ["Distance", "LoadWeight", "AvgSpeed", "TrafficIndex", "WeatherSeverity"]
target = "ShipmentDelay"

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

# ---------- 6. Visualize the tree (detailed) ----------
# figsize/dpi scaled up so every node's text (feature, threshold, gini,
# samples, value, class, proportion) is readable even for deeper trees
fig, ax = plt.subplots(figsize=(38, 20))
plot_tree(
    model,
    feature_names=features,
    class_names=["On-Time", "Delayed"],
    filled=True,          # color nodes by predicted class
    rounded=True,
    proportion=True,      # show % of samples instead of raw counts too
    impurity=True,        # show gini at every node
    node_ids=True,        # show node number (useful to cross-check with text export)
    precision=3,           # more decimal places on thresholds/gini
    fontsize=10,
    ax=ax
)
plt.title("Decision Tree - Shipment Delay Prediction (full detail)", fontsize=18)
plt.tight_layout()
plt.savefig("CS14_decision_tree.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------- 6b. Text version of the tree (every rule, in order) ----------
# Great for reading exact split conditions without squinting at the image
tree_text = export_text(model, feature_names=features, decimals=2, show_weights=True)
print("\n--- Decision Tree Rules (text form) ---\n")
print(tree_text)
with open("CS14_decision_tree_rules.txt", "w") as f:
    f.write(tree_text)

# ---------- 6c. Optional: high-res Graphviz export (best quality) ----------
# Needs the graphviz Python package AND the Graphviz system binary installed
# (Windows: choco install graphviz / download from graphviz.org and add to PATH)
try:
    import graphviz
    from sklearn.tree import export_graphviz

    dot_data = export_graphviz(
        model,
        out_file=None,
        feature_names=features,
        class_names=["On-Time", "Delayed"],
        filled=True,
        rounded=True,
        proportion=True,
        impurity=True,
        node_ids=True,
        precision=3,
        special_characters=True
    )
    graph = graphviz.Source(dot_data)
    graph.render("CS14_decision_tree_graphviz", format="png", cleanup=True)
    print("\nHigh-res Graphviz tree saved as CS14_decision_tree_graphviz.png")
except ImportError:
    print("\n(Optional) Install 'graphviz' package + Graphviz software for an even sharper tree image:")
    print("  pip install graphviz")

# ---------- 7. Q3: Effect of TrafficIndex ----------
# Inspect tree_.feature / tree_.threshold to find nodes splitting on TrafficIndex,
# or simply compare mean delay rate across TrafficIndex bins:
print("\nDelay rate by TrafficIndex bin:")
print(df.groupby(pd.cut(df["TrafficIndex"], bins=5))[target].mean())

# ---------- 8. Q4: Effect of WeatherSeverity ----------
print("\nDelay rate by WeatherSeverity bin:")
print(df.groupby(pd.cut(df["WeatherSeverity"], bins=5))[target].mean())

# ---------- 9. Q5: Highest-risk trip segment ----------
# Combine Distance, LoadWeight, AvgSpeed into risk segments
risk_view = df.groupby([
    pd.cut(df["Distance"], bins=3),
    pd.cut(df["LoadWeight"], bins=3),
    pd.cut(df["AvgSpeed"], bins=3)
])[target].mean().sort_values(ascending=False)
print("\nTop risk segments (Distance x LoadWeight x AvgSpeed):\n", risk_view.head(10))