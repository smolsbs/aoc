#!/usr/bin/env python3

import re
import itertools
from collections import Counter


def algo_p1(data):
    grid = [[False for _ in range(1000)] for _ in range(1000)]
    for line in data:
        x0, y0, x1, y1 = map(int, re.findall(r'\d+', line))
        for i in range(y0, y1+1):
            if 'turn on' in line:
                grid[i][x0:x1+1] = [True for _ in range(x1-x0+1)]
                continue
            if 'turn off' in line:
                grid[i][x0:x1+1] = [False for _ in range(x1-x0+1)]
                continue
            if 'toggle' in line:
                for j in range(x0, x1+1):
                    grid[i][j] = not grid[i][j]
    on = 0
    for i in grid:
        on += Counter(i)[True]
    print(on)

def algo_p2(data):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in data:
        x0, y0, x1, y1 = map(int, re.findall(r'\d+', line))
        for i in range(y0, y1+1):
            if 'turn on' in line:
                grid[i][x0:x1+1] = [j+1 for j in grid[i][x0:x1+1]]
                continue
            if 'turn off' in line:
                grid[i][x0:x1+1] = [0 if j-1 < 0 else j-1 for j in grid[i][x0:x1+1]]
                continue
            if 'toggle' in line:
                grid[i][x0:x1+1] = [j+2 for j in grid[i][x0:x1+1]]
    bright = sum([i for x in grid for i in x])
    print(bright)


def main():
    with open('input', 'r') as fp:
        data = fp.read().split('\n')
    algo_p1(data)
    algo_p2(data)


if __name__ == '__main__':
    main()
