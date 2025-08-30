import json

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for country in f:
        data = json.loads(country)
        if data['title']=='イギリス':
            break
print(data)