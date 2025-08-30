import MeCab
m=MeCab.Tagger()
text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""
result=m.parse(text)
result=result.split('\n')
for word in result:
    lists=word.split(',')
    for list in lists:
        if '\t' in list:
            w,v=list.split('\t')
            if v=='動詞':
                print(w)