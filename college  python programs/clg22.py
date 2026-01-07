import pandas as pd
df = pd.read_excel('https://froyotechnologies.in/TempResources/OrdersExcel.xlsx')
df.head(2)
df.info()
df['City'].isna().sum()
df['City'].fillna('NA', inplace=True)
df['City'].isna().sum()
