# 50
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

words, vectors, word_to_index = load_word2vec('data/GoogleNews-vectors-negative300.bin')
print(vectors[word_to_index['United_States']])
