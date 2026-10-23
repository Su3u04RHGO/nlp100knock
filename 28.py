# 28
import re
import pandas as pd
from pprint import pprint

df = pd.read_json('data/jawiki-country.json.gz', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]
uk_texts = uk_text.split('\n')

pattern = re.compile(r'\|(.+?)\s=\s*(.+)')
clean_stress = re.compile(r'(\'{2,5})(.+?)\1')
clean_link = re.compile(r'\[\[(.+\||)(.+?)\]\]')
mk1 = re.compile(r'\{\{(.+\||)(.+?)\}\}')
mk2 = re.compile(r'\[\[(.+\||)(.+?)\]\]')
mk3 = re.compile(r'<(.*?)\s*.*?/(\1?)>')

ans = {}
for line in uk_texts:
  r = re.search(pattern, line)
  if r:
    a = clean_stress.sub(r'\2', r[2])
    b = clean_link.sub(r'\2', a)
    c = mk1.sub(r'\2', b)
    d = mk2.sub(r'\2', c)
    e = mk3.sub('', d)
    ans[r[1]] = e
pprint(ans)
