import pandas as pd
#series are one-dimensional labeled array capable of holding any data type 
data = [100,102,104]
series = pd.Series(data, index = ['a', 'b', 'c'])
print(series.loc['b'])
series.loc['b'] = 200
print(series.loc['b'])
