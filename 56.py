# 56
import numpy as np
from scipy.stats import spearmanr

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

word_vec_sim = []
human_sim = []
with open('data/wordsim353/combined.csv', 'r', encoding='utf-8') as f:
  for line in f:
    if line.strip():
      w1, w2, v = line.strip().split(',')
      if (w1 in words) and (w2 in words):
        word_vec_sim.append(cossim(vectors[word_to_index[w1]], vectors[word_to_index[w2]]))
        human_sim.append(v)

correlation, p_value = spearmanr(word_vec_sim, human_sim)
print(f'Spearman correlation: {correlation}')
      
      
