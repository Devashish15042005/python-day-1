import pandas as pd
df = pd.read_excel(r'C:\Users\Lenovo\Desktop\PYTHON\froyo_tech\OrdersExcel.xlsx')
print(df.columns)
df['Years'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df.pivot_table(index='Mont', columns='Month', values='Sales', aggfunc='sum', fill_value=0)