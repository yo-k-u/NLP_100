f=open('popular-names.txt','r+')
line=f.readlines()
f.close()
print(len(line))

#wc -l popular-names.txt