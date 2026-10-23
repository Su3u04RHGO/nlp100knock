# 38
import gzip
import json
import re
import MeCab
from collections import Counter
import math

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
japan_words_counter = Counter()
all_words_counter = Counter()
article_count = 0

with gzip.open("data/jawiki-country.json.gz", "rt", encoding="utf-8") as f:
  for line in f:
    article = json.loads(line)
    title = article["title"]
    text = article["text"]
    #print(text[:300])
    clean_text= remove_markup(text)
    
    node = tagger.parseToNode(clean_text)
    words = []
    article_count += 1
    
    while node:
      word = node.surface
      features = node.feature.split(',')
      part_of_speech = features[0]
      if part_of_speech == "名詞" :
        words.append(word)
      node = node.next
    
    if title == "日本":
      japan_words_counter.update(words)
    all_words_counter.update(set(words))

#print(all_words_counter)
#print(japan_words_counter)
results = {}
for word, count in japan_words_counter.items():
  #print(f"{word}, {count}")
  #tf = count / len(japan_words_counter)
  tf = count
  idf = math.log(article_count / int(all_words_counter[word]))
  #print(f"TF={tf}, IDF={idf}, TF・IDF={tf * idf}")
  results[word] = {
    "tf": tf,
    "idf": idf,
    "tfidf": tf * idf
  }

sorted_results = sorted(
  results.items(), 
  key=lambda x: x[1]["tfidf"],
  reverse=True
)

print("単語\tTF\tIDF\tTF・IDF")
for word, scores in sorted_results[:20]:
  print(f"{word}\t{scores['tf']}\t{scores['idf']}\t{scores['tfidf']}")
#for word, count in all_words_counter.most_common(20):
  #print(f"{word}: {count}")
