# 31
import MeCab

text = open('data/sample.txt', encoding='utf-8').read()

tagger = MeCab.Tagger()
node = tagger.parseToNode(text)

while node:
  word = node.surface  # 単語そのもの
  features = node.feature.split(',')  # 品詞などの情報がカンマ区切りで入っている
  part_of_speech = features[0]  # 最初の要素が「品詞」
  base = features[10]
  
  if part_of_speech == "動詞":
    print(word, features[10])
    
  node = node.next  # 次の単語に進む

