import pandas as pd
df = pd.read_csv(r'C:\Users\Lenovo\Desktop\PYTHON\froyo_tech\svmdataset.csv')
df.head(2)
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingModuleSource]
plt.scatter(df['X'], df['Y'])
plt.show()
X= df[['X']]
Y= df['Y']
from sklearn.svm import SVR  # pyright: ignore[reportMissingModuleSource]
svr_lin = SVR(kernel='linear')
svr_lin.fit(X, Y)
svr_lin.score(X, Y)
svr_poly = SVR(kernel='poly')
svr_poly.fit(X, Y)
svr_poly.score(X, Y)
svr_rbf = SVR(kernel='rbf')
svr_rbf.fit(X, Y)
svr_rbf.score(X, Y)
df['lin']= svr_lin.predict(X)
df['poly']= svr_poly.predict(X)
df['rbf']= svr_rbf.predict(X)
plt.scatter(df['X'], df['Y'], label='Original')
plt.plot(df['X'], df['lin'], label='Linear')
plt.plot(df['X'], df['poly'], label='Polynomial')
plt.plot(df['X'], df['rbf'], label='RBF')
plt.legend()
plt.show()
