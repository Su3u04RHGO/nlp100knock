# 33
import spacy

text = open('data/sample.txt', encoding='utf-8').read()
nlp = spacy.load('ja_ginza')

doc = nlp(text)
for token in doc:
  print(token.text, token.head, sep='\t')

