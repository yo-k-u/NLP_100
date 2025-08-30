import re
text='I am an NLPer'
def n_gram(n,text):
    text=re.sub(' ','',text)
    list=[]
    for i in range(len(text)-n+1):
        list.append(text[i:i+n])
    print(list)
n_gram(3,text)