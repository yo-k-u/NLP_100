f=open('popular-names.txt','r+')
line=f.readlines()
f.close()
def output_n(line,N):
    for i in range(N):
        w=line[i].split('\t'or'\n')
        print(w[0])
output_n(line,len(line))

#head -10 popular-names.txt|cut -f 1