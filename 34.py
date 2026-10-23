# 34
import spacy

text = open('data/sample.txt', encoding='utf-8').read()
nlp = spacy.load('ja_ginza')

doc = nlp(text)
for token in doc:
  if token.text == 'メロス' and token.dep_ == 'nsubj':
    print(token.head.text)
  #print(token.text, token.dep_, token.head.text, sep='\t')

