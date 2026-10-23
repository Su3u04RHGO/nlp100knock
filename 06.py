# 06
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

seq1 = "paraparaparadise"
seq2 = "paragraph"

X = gen_ngram(seq1, 2)
Y = gen_ngram(seq2, 2)

# 和集合 (Union)
union_xy = set(X).union(set(Y))          # または X | Y
# 積集合 (Intersection)
intersection_xy = set(X).intersection(set(Y))  # または X & Y
# 差集合 (Difference)
diff_xy = set(X).difference(set(Y)) 

print(f"和集合 {union_xy}")
print(f"積集合 {intersection_xy}")
print(f"差集合 {diff_xy}")

print(f"se in X = {"se" in X}")
print(f"se in Y = {"se" in Y}")
