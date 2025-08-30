import string
word1='パトカー'
word2='タクシー'
word=''
for i in range(len(word1)+len(word2)):
    if i%2==0:
        word=f"{word}{word1[i//2]}"
    else:
        word=f"{word}{word2[i//2]}"
print(word)