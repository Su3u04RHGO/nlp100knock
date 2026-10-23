# 35
import spacy
from spacy import displacy

text = open('data/sample.txt', encoding='utf-8').read()
nlp = spacy.load('ja_ginza')

doc = nlp(text)
html = displacy.render(doc, style='dep', page=True)
with open('graph35.html', 'w', encoding='utf-8') as f:
  f.write(html)
