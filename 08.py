# 08
def cipher(text):
  data = ""
  for c in text:
    if c.islower():
      data += chr(219 - ord(c))
    else:
      data += c
  return data

input = "this is a message."
print(cipher(input))
