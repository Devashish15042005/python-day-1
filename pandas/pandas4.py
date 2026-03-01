import pandas as pd
df = pd.read_csv("jojo_dataset.csv", index_col= "Character")
Missing_person = input("Enter the name of the character you want to search for: ")
try:
    print(df.loc[Missing_person])
except KeyError:
    print(f"{Missing_person} not found in the dataset.")