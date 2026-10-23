# 04
import re

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = re.split(r'[, ]', text.replace('.', ''))
# print(words)

a = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result_dict = {}
for i,word in enumerate(words):
  if (i+1) in a:
    key = word[0]
  else:
    key = word[0:2]
  result_dict[key] = i

print(result_dict)
