
result = []

with open('output3.txt', 'r') as f:
    for line in f:
        newLine = int(line)
        year = newLine % 10000
        result.append(year)
    newResult = dict((x,result.count(x)) for x in set(result))

newResult = {x: newResult.get(x) * 178598027 / 5000 for x in newResult}

print(newResult)

