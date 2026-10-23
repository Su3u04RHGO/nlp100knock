# 55
import numpy as np

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

words, vectors, word_to_index = load_word2vec('data/GoogleNews-vectors-negative300.bin')
stats = {
  'semantic': {'correct': 0, 'incorrect': 0},
  'syntactic': {'correct': 0, 'incorrect': 0}
}
with open('ans54.txt', 'r', encoding='utf-8') as f:
  for line in f:
    words = line.split()
    w1, w2 = words[-3:-1]
    category = 'syntactic' if 'gram' in words[0][:4] else 'semantic'
    result = 'correct' if w1 == w2 else 'incorrect'
    stats[category][result] += 1

print(f"semantic analogy = {stats['semantic']['correct']/(stats['semantic']['correct'] + stats['semantic']['incorrect'])}")
print(f"syntactic analogy = {stats['syntactic']['correct']/(stats['syntactic']['correct'] + stats['syntactic']['incorrect'])}")
