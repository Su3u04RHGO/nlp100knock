# 26
import re
import pandas as pd
from pprint import pprint

df = pd.read_json('data/jawiki-country.json.gz', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]
uk_texts = uk_text.split('\n')

pattern = re.compile(r'\|(.+?)\s=\s*(.+)')
clean_stress = re.compile(r'(\'{2,5})(.+?)\1')
ans = {}
for line in uk_texts:
  r = re.search(pattern, line)
  if r:
    r2 = clean_stress.sub(r'\2', r[2])
    ans[r[1]] = r2
pprint(ans)
