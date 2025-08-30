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
1. 花びらの 舞い散る道を 一緒行く
2. 桜咲く 笑顔の中に 君がいる
3. 蕾から 色づく頃に 夢が芽生え
4. さくらんぼ ひとつ落ちて 風となる
5. 桜舞う 時間（とき）を忘れて お花見ど
6. 夜桜の 月に照らされて 夢の中
7. 散りゆくよ 幸せの影を 織りなして
8. 桜並木 思い出辿る 一歩ずつ
9. 春の風 桜の香りに 包まれつ
10. 桜散る 過去も未来も 一緒にいて

この10個のそれぞれの川柳を10段階で評価してください。
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