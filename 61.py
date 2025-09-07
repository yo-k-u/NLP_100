train_data=[]
with open("train.tsv") as f:
    lines = f.readlines()
    for line in lines:
        line=line.replace("\n","")
        word=line.split("\t")
        words=word[0].split(" ")
        for words in words:
            print(words)
        if word[1]=="0":
            count0=count0+1
        elif word[1]=="1":
            count1=count1+1
    print(f"positive:{count0},negative{count1}")
dev_data=[]
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