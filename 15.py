# 15
import sys
import pandas as pd
import numpy as np

df = pd.read_csv("data/popular-names.txt", sep='\t', header=None)
N=sys.argv[1]
df_list = np.array_split(df, int(N))

for i, sub_df in enumerate(df_list):
  file_name = f"ans15_{i}.txt"
  pd.DataFrame(sub_df).to_csv(file_name, sep='\t', index=False)
