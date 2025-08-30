import random
text='I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
word=text.split(' ')
for i in range(len(word)):
    if len(word[i])>4:
        for j in range(len(word[i])):
            if j!=0 and j!=len(word[i]):
                n1=random.randint(1,len(word[i])-2)
                n2=random.randint(1,len(word[i])-2)
                w=list(word[i])
                w1=w[n1]
                w2=w[n2]
                w[n1]=w2
                w[n2]=w1
                word[i]=''.join(w)
print(word)
                