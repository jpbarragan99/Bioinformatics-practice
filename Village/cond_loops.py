starPos = 100
endPos = 200
result = 0

for x in range(starPos, endPos + 1):
    if x % 2 != 0:
        result += x

print (result)