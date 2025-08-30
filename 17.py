f=open('popular-names.txt','r+')
line=f.readlines()
f.close()
def output_n(line,N):
    list=[]
    for i in range(N):
        w=line[i].split('\t'or'\n')
        print(w[0])
        list.append(w[0])
    return list  
print(set(output_n(line,10)))

#head popular-names.txt|cut -f 1|uniq