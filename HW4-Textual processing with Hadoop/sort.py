from sys import stdin


with open('hw5_speech1_part-00000.txt', 'r') as f:
    i = 0
    dict = {}
    for line in f:
        newline = line.strip()
        print(newline)
        _line = newline.replace('(','').replace(')','')
        word, fre = _line.split(' ')
        print(word, fre)
        if fre.isnumeric():
            count = float(fre)
            # dict[i].update({word:count})
            dict[word] = count
        else:
            pass
    print(dict)