import pandas as pd
df=pd.read_excel('https://froyotechnologies.in/TempResources/NaiveData.xlsx') 
print(df.head(2))
print(df['Case'].value_counts())
df['Case1']=df["Case"].replace({'Sunny':1, 'Rainy':2, 'Overcast':3})
x=df[['Case1']] 
y=df['Play']
from sklearn.naive_bayes import GaussianNB
gb=GaussianNB()
gb.fit(x,y)
print(gb.score(x,y))
df['Play1']= gb.predict(x) 
print(pd.crosstab(df['Play'], df['Play1'], margins=True))