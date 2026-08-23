import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv(r"C:\Users\Lenovo\Desktop\PYTHON\froyo_tech\CS16DataSet.csv")

# Features
features = ['Age', 'BMI', 'GlucoseLevel', 'BloodPressure', 'PhysicalActivity']
X = df[features]

# Scale and cluster
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Pairplot
sns.pairplot(df, vars=features, hue='Cluster', palette='viridis')
plt.savefig("pairplot_clusters.png")
plt.show()