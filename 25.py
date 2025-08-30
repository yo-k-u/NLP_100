import json
import re

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for country in f:
        data = json.loads(country)
        if data['title']=='イギリス':
            data=str(data)
            break
print(data)
data=re.findall(r'{{基礎情報.*?}}',data)
data=re.findall(r'.*?=.*?(?:{{.*?}}|\|)',data[0])
dict={}
for data in data:
    data=data.split("=")
    # string=re.findall(r'|(.*?)',data)
    dict[data[0]]=data[1]
print(dict)