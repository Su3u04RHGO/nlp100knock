# 21
import pandas as pd

df = pd.read_json("data/jawiki-country.json.gz", lines=True)

uk_text = df.query('title == "イギリス"')['text']
category_pattern = r'\[\[Category:.*\]\]'
category_lines = uk_text.str.findall(category_pattern)
print(*category_lines.values[0], sep='\n')

#lines = uk_text.split('\n')

#for line in lines:
#  if "[[Category:" in line:
#    print(line)
