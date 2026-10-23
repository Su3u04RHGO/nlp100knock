# 17
import pandas as pd

df = pd.read_csv("data/popular-names.txt", sep='\t', header=None)
first_column = df.iloc[:, 0]
print(first_column.drop_duplicates().sort_values())
