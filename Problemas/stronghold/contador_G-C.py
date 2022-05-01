def readFile (filePath):
    with open (filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def gc_content(seq):
  return round(
    ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)

FASTAFile = readFile("test_data/gc_content.txt")

FASTADic = {}

FASTALabel = ""

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADic[FASTALabel]= ""
    else:
        FASTADic[FASTALabel] += line

RESULTDic = {key: gc_content(value) for (key, value) in FASTADic.items()}

print (RESULTDic)

MaxGCKey = max(RESULTDic, key=RESULTDic.get)

print(f'{MaxGCKey[1:]}\n{RESULTDic[MaxGCKey]}')
