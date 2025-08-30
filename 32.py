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
n=0
for i in range(len(result)):
    lists=result[i].split(',')
    for j in range(len(lists)):
        if '\t' in lists[j]:
            w,v=lists[j].split('\t')
            if n==0:
                if v=='名詞':
                    n=1
            else:
                if n==1:
                    if w=='の':
                        n=2
                    else:
                        n=0
                else:
                    if n==2:
                        if v=='名詞':
                            n=3
                        else:
                            n=0
                    else:
                        if n==3:
                            w0,v0=(result[i-3].split(','))[0].split('\t')
                            w1,v1=(result[i-2].split(','))[0].split('\t')
                            w2,v2=(result[i-1].split(','))[0].split('\t')
                            print(w0+w1+w2)
                            n=0
