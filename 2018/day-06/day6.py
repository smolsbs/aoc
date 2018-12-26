#!/usr/bin/env python3


def manhattan(a, b):
    return sum(abs(a - b) for a, b in zip(a, b))


def main():
    data = set()
    with open('sinput', 'r') as fp:
        data.add(tuple(map(int, x.split(", "))) for x in fp.readlines())
    print(data.)
    max_x = max(list(zip(*data))[0])
    max_y = max(list(zip(*data))[1])
    chart = [[0 for _ in range(max_y)] for _ in range(max_x)]
    for i, x, y in enumerate(data):
        chart[x-1][y-1] = i

    print(chart)       
if __name__ == '__main__':
    main()