#t-SNEは次元圧縮
from gensim.models import KeyedVectors
import pycountry
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
country_names=[country.name for country in pycountry.countries]
model=KeyedVectors.load_word2vec_format('C:\\Users\\ky200\\Downloads\\GoogleNews-vectors-negative300.bin', binary=True)
vec=[]
label=[]
for country in country_names:
    try:
        vec.append(model[country])
        label.append(country)
    except KeyError:
        continue
tsne=TSNE(n_components=2,random_state=0, perplexity=len(vec)-1)
vec=np.vstack(vec)
xy=tsne.fit_transform(vec)
plt.scatter(xy[:,0],xy[:,1])
plt.show()