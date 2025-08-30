import random
f=open('popular-names.txt','r+')
line=f.readlines()
f.close()
list=[i for i in range(len(line))]
for i in range(len(line)):
    rand=random.randint(0,len(list)-1)
    print(line[rand])
    del list[rand]

#shuf popular-names.txt -o output.txt