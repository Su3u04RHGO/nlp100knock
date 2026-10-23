# 09
import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = text.split()

result = []
for word in words:
  if len(word) <= 6:
    result.append(word)
  else:
    a = word[1:len(word)-1]
    random_a = list(a)
    random.shuffle(random_a)
    join_random_a = "".join(random_a)
    result.append(word[0] + join_random_a + word[len(word)-1])

print(result)

