from gensim.models import KeyedVectors

model=KeyedVectors.load_word2vec_format('C:\\Users\\ky200\\Downloads\\GoogleNews-vectors-negative300.bin', binary=True)
n=0
d=0
with open("combined.csv","r",) as f:
    lines=f.readlines()
    for line in lines:
        line=line.replace("\n","")
        text=line.split(",")
        try:
            if n!=0:
                d=d+(float(text[2])-model.similarity(text[0],text[1]))**2
            n=n+1
        except KeyError:
            continue
n=n-1
print(1-6*d/(n*(n**2-1)))