# 58
import pycountry
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

def load_word2vec(path):
  with open(path, 'rb') as f:
    vocab_size, dim = map(int, f.readline().split())
    words = []
    vectors = np.empty((vocab_size, dim), dtype=np.float32)
    for i in range(vocab_size):
      chars = []
      while True:
        ch = f.read(1)
        if ch == b' ':
          break
        if ch != b'\n':
          chars.append(ch)
      words.append(b''.join(chars).decode('utf-8'))
      vectors[i] = np.fromfile(f, dtype=np.float32, count=dim)
  word_to_index = {w: i for i, w in enumerate(words)}
  return words, vectors, word_to_index

words, vectors, word_to_index = load_word2vec('data/GoogleNews-vectors-negative300.bin')
countries = []
for country in pycountry.countries:
  countries.append(country.name)

country_names = []
country_vectors = []

for word in words:
  if word in countries:
    country_names.append(word)
    country_vectors.append(vectors[word_to_index[word]])

linkage_result = linkage(country_vectors, method='ward', metric='euclidean')

plt.figure(figsize=(16, 8))
dendrogram(
    linkage_result,
    labels=country_names,
    leaf_rotation=90,
    leaf_font_size=10
)
plt.title("Hierarchical Clustering Dendrogram (Ward's Method)")
plt.xlabel("Country")
plt.ylabel("Distance")
plt.savefig("graph58.png")
