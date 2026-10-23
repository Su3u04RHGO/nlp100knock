# 24
import pandas as pd

df = pd.read_json("data/jawiki-country.json.gz", lines=True)
uk_text = df.query('title == "イギリス"')['text']


media_file_pattern = r'(?m)\[\[(?:ファイル|File):([^|\]]+)'
raw_media_files = uk_text.str.findall(media_file_pattern)
print(raw_media_files.values[0])

#sections = [f"{name}, {len(eq)-1}" for eq, name in raw_sections.values[0]]
#print(*sections, sep='\n')
