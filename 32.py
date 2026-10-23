# 32
import MeCab

text = open('data/sample.txt', encoding='utf-8').read()

tagger = MeCab.Tagger()
node = tagger.parseToNode(text)
words = []

while node:
  word = node.surface  # 単語そのもの
  features = node.feature.split(',')  # 品詞などの情報がカンマ区切りで入っている
  part_of_speech = features[0]  # 最初の要素が「品詞」
  words.append({'surface': word, 'pos': part_of_speech})
  node = node.next  # 次の単語に進む

for i in range(len(words) - 2):
  w1 = words[i]
  w2 = words[i+1]
  w3 = words[i+2]
  
  if (w1['pos'] == '名詞' and 
      w2['surface'] == 'の' and
      w3['pos'] == '名詞'):
    print(w1['surface']+w2['surface']+w3['surface'])
