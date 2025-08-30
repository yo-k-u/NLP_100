from gensim.models import KeyedVectors
import urllib.request

model=KeyedVectors.load_word2vec_format('C:\\Users\\ky200\\Downloads\\GoogleNews-vectors-negative300.bin', binary=True)
with urllib.request.urlopen("http://download.tensorflow.org/data/questions-words.txt") as f:
    line=f.read().decode("utf-8").split("\n")
    r=0
    n=0
    for l in line:
        n=n+1
        text=l.split(" ")
        if len(text)<3:
            continue
        ans=model.most_similar(positive=model[text[1]]-model[text[0]]+model[text[2]],topn=1)
        if ans[0][0]==text[2]:
            r=r+1
            print(str(r/n))