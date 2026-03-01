import pandas as pd
df = pd.read_csv("jojo_dataset.csv", index_col= "Character")
#Selecting a column
print(df)
print(df["Stand_Name"].to_string())
print(df["Role"].to_string())
print(df["Part"].to_string())
#Selecting a row
print(df.loc["Jobin Higashikata"])
print(df.loc["Jonathan Joestar":"Dio Brando", ["Stand_Name", "Role"]])