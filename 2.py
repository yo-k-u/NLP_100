text='stressed'
word=''
for i in range(len(text)):
    word=f"{word}{text[len(text)-i-1]}"
print(word)