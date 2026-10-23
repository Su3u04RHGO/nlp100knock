# 20
import pandas as pd

df = pd.read_json("data/jawiki-country.json.gz", lines=True)
uk_text = df.query('title == "イギリス"')['text']
print(uk_text.values[0])
