f=open('popular-names.txt','r+')
line=f.readlines()
f.close()
def output_n(line,N):
    for i in range(N):
        print(line[i])
output_n(line,10)
#head -10 popular-names.txt