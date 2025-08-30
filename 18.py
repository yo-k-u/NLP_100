f=open('popular-names.txt','r+')
line=f.readlines()
f.close()
def output_n(line,N):
    list=[]
    listn=[]
    for i in range(N):
        w=line[i].split('\t'or'\n')
        print(w[0])
        if w[0] not in list:
            list.append(w[0])
            listn.append(1)
        else:
            listn[list.index(w[0])]=listn[list.index(w[0])]+1
    dic=dict(zip(list,listn))
    sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1],reverse=True))
    print(sorted_dict)
    return sorted_dict
output_n(line,len(line))

#cut -d' ' -f1 popular-names.txt | sort | uniq -c | sort -nr