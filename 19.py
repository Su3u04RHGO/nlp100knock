# 19
import pandas as pd

df = pd.read_csv("data/popular-names.txt", sep='\t', header=None)
print(df.sort_values(by=df.columns[3], ascending=False))
