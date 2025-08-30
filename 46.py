import requests
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
text="""
お題を桜として、
川柳を10個作成してください。
"""

data={
    "model":"gpt-4o-mini",
    "messages":[
        {"role":"user","content":text}
    ]
}
r=requests.post('https://api.openai.com/v1/chat/completions',headers=header,json=data)
result=r.json()
print(result["choices"][0]["message"]["content"])