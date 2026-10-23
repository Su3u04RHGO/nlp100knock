# 12
import pandas as pd
df = pd.read_csv("data/popular-names.txt", sep='\t', header=None)
N = 10
print(df.tail(N))
