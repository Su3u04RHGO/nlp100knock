# 36
import gzip
import json
import re
import MeCab
from collections import Counter

def remove_markup(text):
  #強調マークアップ除去
  text = re.sub(r"(\'{2,5})(.+?)\1", r"\2", text)
  #内部リンクマークアップ除去
  #text = re.sub(r"\[\[(.+\||)(.+?)\]\]", r"\2", text)
  text = re.sub(r'\[\[(?:[^|\]]*?\|)??([^|\]]+?)\]\]', r'\1', text)
  #外部リンクマークアップ除去
  #text = re.sub(r"\[http.?:.*\]", "", text)
  text = re.sub(r'\[http.?://[^\]]+\]', '', text)
  #HTMLタグ除去
  text = re.sub(r"<[^>]+>", "", text)
  #テンプレートマークアップ除去
  #text = re.sub(r"\{\{(.+\||)(.+?)\}\}", r"\2", text)
  text = re.sub(r'\{\{.*?\}\}', '', text)
  return text

tagger = MeCab.Tagger()
all_words_counter = Counter()

with gzip.open("data/jawiki-country.json.gz", "rt", encoding="utf-8") as f:
  for line in f:
    article = json.loads(line)
    title = article["title"]
    text = article["text"]
    #print(text[:300])
    clean_text= remove_markup(text)
    
    node = tagger.parseToNode(clean_text)
    words = []
    while node:
      if node.surface:
        words.append(node.surface)
      node = node.next
    all_words_counter.update(words)
    
for word, count in all_words_counter.most_common(20):
  print(f"{word}: {count}")
    


