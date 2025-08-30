f=open('popular-names.txt','r+')
line=f.readlines()
f.close()
def output_n(line,N):
    for i in range(N):
        f=open(f'popular-names{str(i)}.txt','a+')
        for j in range(len(line)//N):
            f.write(line[i*N+j])
output_n(line,10)
#split -n 10 popular-names.txt popular-names