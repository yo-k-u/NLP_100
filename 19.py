f=open('popular-names.txt','r+')
line=f.readlines()
f.close()
def output_n(line,N):
    list=[line[i].split('\t'or'\n') for i in range(N)]
    for i in range(N-1):
        for j in range(i,N-1):
            if int(list[j][2])>int(list[j+1][2]):
                list[j],list[j+1]=list[j+1],list[j]
    print(list)
output_n(line,len(line))

#sort -k 3,3n popular-names.txt