# 10
import pandas as pd
df = pd.read_csv("data/popular-names.txt", sep='\t', header=None)
print(len(df))
