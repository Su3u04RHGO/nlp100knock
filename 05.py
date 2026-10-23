# 05
import re
def gen_ngram(sequence, n):
  ngram = []
  seq_len = len(sequence)
  for i, c in enumerate(sequence):
    if (i + n) > seq_len:
      break
    else:
      ngram.append(sequence[i:i+n])
  return ngram

seq = "I am an NLPer"
print(f"tri-gram, {gen_ngram(seq, 3)}")
print(f"bi-gram, {gen_ngram(seq, 2)}")
