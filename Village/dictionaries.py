txtStr= "We tried list and we tried dicts also we tried Zen"

wordCountDic = {}

for word in txtStr.split(' '):
    if word in wordCountDic:
        wordCountDic[word] +=1
    else:
        wordCountDic[word] = 1

for key, value in wordCountDic.items():
        print(key, value)