import pandas as pd

url = "https://froyotechnologies.in/TempResources/retail_sales.csv"

df = pd.read_csv(url)
pivot = df.pivot_table(
    values="TotalPrice",
    index="Product",
    columns="City",
    aggfunc="sum"
)

print(pivot)
