f=open('popular-names.txt','r+')
line=f.readlines()
f.close()
def output_n(line,N):
    for i in range(len(line)-1-N,len(line)-1):
        print(line[i])
output_n(line,10)
#tail -10 popular-names.txt