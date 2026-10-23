# 25
import pandas as pd
from pprint import pprint

df = pd.read_json("data/jawiki-country.json.gz", lines=True)
uk_text = df.query('title == "イギリス"')['text']
#print(uk_text.values[0])

pattern1 = r'(\{\{基礎情報[\s\S]*?\n\}\})'
a = uk_text.str.extract(pattern1)[0]
#print(*a.values[0], sep='\n')
#print(type(a))

#pattern2 = r'(?m)^\|(.*)?[\s\S]*?=[\s\S]*?.+$'
pattern2 = r'(?m)^\|([^=\s]+?)\s*=\s*(.+?)$'
b = a.str.findall(pattern2)
#print(b.values[0])

b_dict = dict(b.values[0])
pprint(b_dict)

