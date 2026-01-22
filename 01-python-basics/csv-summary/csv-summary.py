import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), "Data.csv")
df = pd.read_csv(file_path)
print("Rows:",df.shape[0])
print("Columns:",df.shape[1])
print(df.head())
print("Column Names:", df.columns.tolist())