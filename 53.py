from gensim.models import KeyedVectors

model=KeyedVectors.load_word2vec_format('C:\\Users\\ky200\\Downloads\\GoogleNews-vectors-negative300.bin', binary=True)
vec=model["Spain"]-model["Madrid"]+model["Athens"]
print(model.most_similar(positive=vec,topn=10))