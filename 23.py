import json
import re

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for country in f:
        data = json.loads(country)
        if data['title']=='イギリス':
            data=str(data)
            break
data1=re.findall(r'\=\=(.*?)\=\=', data)
data2=re.findall(r'\=\=\=(.*?)\=\=\=', data)
data3=re.findall(r'\=\=\=\=(.*?)\=\=\=\=', data)

data1=[s for s in data1 if ('=' not in s and s!='')]
data2=[s for s in data2 if ('=' not in s and s!='')]
data3=[s for s in data3 if ('=' not in s and s!='')]

for data in data1:
    print(data+str(':1'))
for data in data2:
    print(data+str(':2'))
for data in data3:
    print(data+str(':3'))