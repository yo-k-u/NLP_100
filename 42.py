import csv
import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
header={
    "Authorization":f"Bearer {os.environ.get('OPEN_API_KEY')}",
    "Content-Type": "application/json"
}
n=0
with open("C:\\Users\\ky200\\Downloads\\high_school_mathematics.csv","r", encoding="utf-8") as f:
    reader=csv.reader(f)
    for row in reader:
        text1=f"{row[0]}   A:{row[1]} B:{row[2]} C:{row[3]} D:{row[4]}   出力はA/B/C/D"
        print(text1)
        data={
            "model":"gpt-4o-mini",
            "messages":[
                {"role":"user","content":text1}
            ],
            "response_format": {
                "type":"json_schema",
                "json_schema":{
                    "name":"mc_answer",
                    "strict":True,
                    "schema": {
                        "type":"object",
                        "properties":{
                            "answer":{"type": "string", "enum": ["A","B","C","D"]}
                        },
                        "required":["answer"],
                        "additionalProperties": False,
                    },
                },
            },
        }
        r=requests.post('https://api.openai.com/v1/chat/completions',headers=header,json=data)
        result=r.json()
        data=json.loads(result["choices"][0]["message"]["content"])
        ans=data["answer"]
        if ans==row[5]:
            n=n+1
            print(ans)
print(n)