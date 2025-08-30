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
shot1="""
日本の近代化に関連するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

ア　府知事・県令からなる地方官会議が設置された。
イ　廃藩置県が実施され，中央から府知事・県令が派遣される体制になった。
ウ　すべての藩主が，天皇に領地と領民を返還した。

解答: ウ→イ→ア
"""
shot2="""
江戸幕府の北方での対外的な緊張について述べた次の文ア～ウを年代の古い順に正しく並べよ。

ア　レザノフが長崎に来航したが，幕府が冷淡な対応をしたため，ロシア船が樺太や択捉島を攻撃した。
イ　ゴローウニンが国後島に上陸し，幕府の役人に捕らえられ抑留された。
ウ　ラクスマンが根室に来航し，漂流民を届けるとともに通商を求めた。

解答: ウ→ア→イ
"""
shot3="""
中居屋重兵衛の生涯の期間におこったできごとについて述べた次のア～ウを，年代の古い順に正しく並べよ。

ア　アヘン戦争がおこり，清がイギリスに敗北した。
イ　異国船打払令が出され，外国船を撃退することが命じられた。
ウ　桜田門外の変がおこり，大老の井伊直弼が暗殺された。

解答: イ→ア→ウ
"""
shot4="""
加藤高明が外務大臣として提言を行ってから、内閣総理大臣となり演説を行うまでの時期のできごとについて述べた次のア～ウを，年代の古い順に正しく並べよ。

ア　朝鮮半島において，独立を求める大衆運動である三・一独立運動が展開された。
イ　関東大震災後の混乱のなかで，朝鮮人や中国人に対する殺傷事件がおきた。
ウ　日本政府が，袁世凱政府に対して二十一カ条の要求を突き付けた。

解答: ウ→ア→イ
"""
text="""
9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。
"""

data={
    "model":"gpt-4o-mini",
    "messages":[
        {"role":"system","content":shot1},
        {"role":"system","content":shot2},
        {"role":"system","content":shot3},
        {"role":"system","content":shot4},
        {"role":"user","content":text}
    ]
}
r=requests.post('https://api.openai.com/v1/chat/completions',headers=header,json=data)
result=r.json()
print(result["choices"][0]["message"]["content"])