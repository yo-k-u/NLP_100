import re
obj={}
obj_list=[]
with open("train.tsv") as f:
    lines = f.readlines()
    for line in lines:
        line=line.replace("\n","")
        word=line.split("\t")
        if word[1]=='0' or word[1]=='1':
            obj['text']=word[0]
            obj['label']=word[1]
            words=re.findall(r"\w+",word[0])
            features={}
            for words in words:
                if words in features:
                    features[words]=features[words]+1
                else:
                    features[words]=1
            obj["feature"]=features
            obj_list.append(obj)
print(obj_list)
obj={}
obj_list=[]
with open("dev.tsv") as f:
    lines=f.readlines()
    for line in lines:
        line=line.replace("\n","")
        word=line.split("\t")
        if word[1]=='0' or word[1]=='1':
            obj['text']=word[0]
            obj['label']=word[1]
            words=re.findall(r"\w+",word[0])
            features={}
            for words in words:
                if words in features:
                    features[words]=features[words]+1
                else:
                    features[words]=1
            obj["feature"]=features
            obj_list.append(obj)
print(obj_list)