import re
text='Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
word=text.split(' ')
list=[1, 5, 6, 7, 8, 9, 15, 16, 19]
dict0={}
for i in range(len(word)):
    if i in list:
        word[i]=re.sub('[,.]','', word[i])
        dict0[word[i][0]]=i
    else:
        word[i]=re.sub('[,.]','', word[i])
        dict0[word[i][0]+word[i][1]]=i
print(dict0)