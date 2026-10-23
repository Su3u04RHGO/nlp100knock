# 59
import pycountry
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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

tsne = TSNE(n_components=2, random_state=42, perplexity=30)
country_vectors_tsne = tsne.fit_transform(np.array(country_vectors))

kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(country_vectors)

plt.figure(figsize=(16, 8))
x = country_vectors_tsne[:, 0]
y = country_vectors_tsne[:, 1]
plt.scatter(x, y, c=kmeans.labels_, cmap='rainbow', alpha=0.7)
for i, name in enumerate(country_names):
  plt.annotate(name, (x[i], y[i]), fontsize=9, alpha=0.8)
plt.title("t-SNE Visualization of Country Word Vectors")
plt.grid(True)
plt.savefig("graph59.png")
