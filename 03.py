# 03
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = text.replace(',',' ').replace('.',' ').split()
list = []
for word in words:
  list.append(len(word))
print(list)
