#!/usr/bin/env python3
from collections import Counter


def makePlane(n):
    return [['.' for _ in range(n)] for _ in range(n)]

def printPlane(array):
    for line in array:
        print(''.join(line))

def fillPlane(array, nArray, points):
    for i in range(nArray):
        for j in range(nArray):
            if array[j][i] != '.':
                continue
            d = []
            for p in points:
                d.append((p[0], manhattan((i,j),(p[1],p[2]))))
            d = sorted(d, key=lambda x: x[1])
            if d[0][1] < d[1][1]:
                array[j][i] = d[0][0]

def getAllEdgeNumbers(array):
    edges = set()
    n = len(array)
    for c in range(n):
        # left and right bounds
        if array[c][0] not in edges:
            edges.add(array[c][0])
        if array[c][-1] not in edges:
            edges.add(array[c][-1])
        # upper and lower bounds
        if array[0][c] not in edges:
            edges.add(array[0][c])
        if array[-1][c] not in edges:
            edges.add(array[-1][c])
    edges.remove('.')
    return edges

def manhattan(a, b):
    return sum(abs(a - b) for a, b in zip(a, b))


def main():
    
    data = set()
    with open('input', 'r') as fp:
        i = 1
        for line in fp.read().strip().split('\n'):
            data.add(tuple([str(i)] + list(map(int, line.split(', ')))))
            i += 1
    x = sorted(data, key=lambda x: x[2], reverse=True)[0][2]
    y = sorted(data, key=lambda x: x[1], reverse=True)[0][1]
    n = max(x, y) +1
    plane = makePlane(n)
    for p in data:
        plane[p[2]][p[1]] = p[0]
        
    fillPlane(plane, len(plane), data)

    e = getAllEdgeNumbers(plane)
    biggest = Counter()
    print(e)
    for line in plane:
        for c in line:
            if c == '.':
                continue
            biggest.update(c)
    
    for p in e:
        del biggest[p]
    

    print(biggest.most_common(5))

    # printPlane(plane)
if __name__ == '__main__':
    main()