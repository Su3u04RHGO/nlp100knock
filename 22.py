# 22
import pandas as pd

df = pd.read_json("data/jawiki-country.json.gz", lines=True)
uk_text = df.query('title == "イギリス"')['text']
#print(uk_text)

#category_pattern = r'\[\[Category:.*\]\]'
category_pattern = r'\[\[Category:(.*)\]\]'
category_names = uk_text.str.findall(category_pattern)
#print(category_names.values[0])
print(*category_names.values[0], sep='\n')


