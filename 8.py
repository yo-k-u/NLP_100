def cipher(text1):
    text2=''
    for i in range(len(text1)):
        if ord(text1[i])>=ord('a') and ord(text1[i])<=ord('z'):
            text2=text2+str(ord(text1[i]))
        else:
            text2=text2+str(text1[i])
    return text2
print(cipher('ABdadfA'))