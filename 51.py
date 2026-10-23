# 51
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

def cosine_similarity(vec_a, vec_b):
  vec_a_dot_vec_b = 0
  vec_a_norm_square = 0
  vec_b_norm_square = 0
  for i in range(len(vec_a)):
    vec_a_dot_vec_b += vec_a[i] * vec_b[i]
    vec_a_norm_square += vec_a[i] * vec_a[i]
    vec_b_norm_square += vec_b[i] * vec_b[i]
  return vec_a_dot_vec_b / (math.sqrt(vec_a_norm_square) * math.sqrt(vec_b_norm_square))

def cossim(vec_a, vec_b):
  return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

words, vectors, word_to_index = load_word2vec('data/GoogleNews-vectors-negative300.bin')
a = vectors[word_to_index['United_States']]
b = vectors[word_to_index['U.S.']]

print(cosine_similarity(a,b))
print(cossim(a,b))
