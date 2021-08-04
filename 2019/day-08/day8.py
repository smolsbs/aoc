#!/usr/bin/env python3

import AoCUtils
from collections import defaultdict, Counter

def getCounterLayer(layer, n):
    _sum = 0
    for l in layer:
        _sum += Counter(l)[n]
    return _sum
    
def check(layers):
    c = []
    for k,v in layers.items():
        _sum = 0
        for l in v:
            _sum += Counter(l)[0]

        c.append((k, _sum))
    lowest = sorted(c, key=lambda x: x[1])[0][0]

    return getCounterLayer(layers[lowest], 1) * getCounterLayer(layers[lowest], 2)


def getPicture(layers, width, length):
    finalPicture = [[2 for _ in range(width)] for x in range(length)]

    (x, y) = 0, 0
    total = width * length
    j = 0
    while j < total:
        for i in range(100):
            if layers[i][y][x] != 2:
                if layers[i][y][x] == 0:
                    finalPicture[y][x] = ' '
                    break
                elif layers[i][y][x] == 1:
                    finalPicture[y][x] = '#'
                    break
            finalPicture[y][x] = ' '
        j+= 1
        (x, y) = j % width, j // width

    for x in finalPicture:
        print(''.join(x))


def main():
    data = AoCUtils.loadInput('input')[0]

    (width, lenght) = 25, 6
    layers = defaultdict(dict)

    for i in range(len(data)// (width* lenght)):
        layer = []
        for _ in range(lenght):
            layer.append(  [int(x) for x in data[:width]]  )
            data = data[width:]
        
        layers[i] = layer
    
    p1 = check(layers)

    print(p1)
    getPicture(layers, width, lenght)

if __name__ == '__main__':
    main()