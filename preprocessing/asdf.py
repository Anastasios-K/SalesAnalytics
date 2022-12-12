import os
import pandas as pd

df = pd.read_excel(os.path.join("data", "Sales.xls"))
df.drop(columns=["Row ID"], inplace=True)


# Count Product ID
print(len(df["Order Date"].unique()))