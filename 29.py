# 29
import re
import pandas as pd
from pprint import pprint
import requests

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
    ans[r[1]] = a
#pprint(ans)

flag_image = ans['国旗画像']
url = "https://www.mediawiki.org/w/api.php"

headers = {
  'User-Agent': 'Track learning platform (+https://tracks.run/)'
}

params = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": f"File:{ans['国旗画像']}",
    "iiprop": "url"
}

data = requests.get(url, headers=headers, params=params)
#print(data.text)
print(re.search(r'"url":"(.*?)"', data.text).group(1))
