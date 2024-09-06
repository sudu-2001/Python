string="i like football"

word=string.split()

word[-1]=word[-1][::-1]

print(word)

updated=' '.join(word)

print(updated)