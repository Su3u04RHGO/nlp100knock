# 52
import numpy as np
import math

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

def cossim(vec_a, vec_b):
  return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

words, vectors, word_to_index = load_word2vec('data/GoogleNews-vectors-negative300.bin')
x = vectors[word_to_index['United_States']]

#print(words)
#print(word_to_index['Diana'])

cossims = []
for word in words:
  if word == 'United_States':
    cossims.append(1.0)
    continue
  y = vectors[word_to_index[word]]
  cossims.append(cossim(x,y))

cossims_np = np.array(cossims)
sorted_indices = np.argsort(cossims_np)[::-1]

print("UNUSED HINT")
for index in sorted_indices[1:11]:
  print(f"{words[index]}: {cossims_np[index]}")
#print(sorted_indices)
#print(cossim(a,b))

def most_similar(positive, negative=None, topn=10):
  if negative is None:
    negative = []
  query = np.zeros(vectors.shape[1], dtype=np.float32)
  exclude = set()
  for w in positive:
    query += vectors[word_to_index[w]]
    exclude.add(w)
  for w in negative:
    query -= vectors[word_to_index[w]]
    exclude.add(w)
  sims = np.dot(vectors, query) / (np.linalg.norm(vectors, axis=1) * np.linalg.norm(query))
  for w in exclude:
    sims[word_to_index[w]] = -np.inf
  top = np.argsort(-sims)[:topn]
  return [(words[i], float(sims[i])) for i in top]

print("USED HINT")
print(*most_similar(['United_States']), sep='\n')
