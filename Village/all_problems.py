txtStr = "We tried list and we tried dicts also we tried Zen"

wordCoutDict = {}

for word in txtStr.split (' '):
    if word in wordCoutDict:
        wordCoutDict[word] += 1
    else:
        wordCoutDict[word] = 1

