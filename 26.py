import json
import re

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for country in f:
        data = json.loads(country)
        if data['title']=='イギリス':
            stress=re.sub(r"'{2,5}", '',str(data['text']))
            print(stress)
            break