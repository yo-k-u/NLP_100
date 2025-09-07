count0=0
count1=0
with open("train.tsv") as f:
    lines = f.readlines()
    for line in lines:
        line=line.replace("\n","")
        word=line.split("\t")
        if word[1]=="0":
            count0=count0+1
        elif word[1]=="1":
            count1=count1+1
    print(f"positive:{count0},negative{count1}")
count0=0
count1=0
with open("dev.tsv") as f:
    lines=f.readlines()
    for line in lines:
        line=line.replace("\n","")
        word=line.split("\t")
        if word[1]=="0":
            count0=count0+1
        elif word[1]=="1":
            count1=count1+1
    print(f"positive:{count0},negative{count1}")