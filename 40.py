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
9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。
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