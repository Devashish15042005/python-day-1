# Dataframe = it is a tabular data structure with labeled axes (rows and columns)
import pandas as pd
data = {'NAME': ['Jonathan', 'Joseph', 'jotaro'],
        'AGE': [50,40,25]}
df = pd.DataFrame(data, index = ['GEN1', 'GEN3', 'GEN6'])
print(df)
#add a new column
df['Power'] = ['Hamon', 'Hamon/Hermit Purple', 'Star Platinum']
#add a new row
new_rows = pd.DataFrame ([{'NAME': 'josuke', 'AGE': 18, 'Power': 'Crazy Diamond'},
                         {'NAME': 'Giorno', 'AGE': 20, 'Power': 'Gold Experience'}], 
                         index = ['GEN4', 'GEN2'])
df = pd.concat([df, new_rows])
print(df)