import re
text='Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
word=text.split(' ')
for i in range(len(word)):
        word[i] = re.sub('[,.]','', word[i])
print(word)