word1='paraparaparadise'
word2='paragraph'
import re
def n_gram(n,text):
    text=re.sub(' ','',text)
    list=[]
    for i in range(len(text)-n+1):
        list.append(text[i:i+n])
    return list
X=n_gram(2,word1)
Y=n_gram(2,word2)
print(set(X)|set(Y))
print(set(X)&set(Y))
print(set(X)-set(Y))
if 'se' in X:
    if 'se' in Y:
        print('se include X and Y')
    else:
        print('NOT EXIST')
else:
    print('NOT EXIST')
