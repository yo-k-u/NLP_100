from gensim.models import KeyedVectors
import pycountry
from sklearn.cluster import AgglomerativeClustering
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
kmeans=AgglomerativeClustering(n_clusters=5).fit(vec)
label1=[]
label2=[]
label3=[]
label4=[]
label5=[]
for i in range(len(kmeans.labels_)):
    if kmeans.labels_[i]==0:
        label1.append(label[i])
    elif kmeans.labels_[i]==1:
        label2.append(label[i])
    elif kmeans.labels_[i]==2:
        label3.append(label[i])
    elif kmeans.labels_[i]==3:
        label4.append(label[i])
    else:
        label5.append(label[i])
print(label1)
print(label2)
print(label3)
print(label4)
print(label5)