# 23
import pandas as pd

df = pd.read_json("data/jawiki-country.json.gz", lines=True)

uk_text = df.query('title == "イギリス"')['text']
#print(uk_text.values[0])

section_pattern = r'(?m)^(={2,})\s*(.*?)\s*\1$'
raw_sections = uk_text.str.findall(section_pattern)
#print(raw_sections.values[0])

sections = [f"{name}, {len(eq)-1}" for eq, name in raw_sections.values[0]]
print(*sections, sep='\n')
