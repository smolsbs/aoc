#!/usr/bin/env python3

import aocUtils
import numpy as np


def solve_part_1(grid:np.ndarray, start: tuple, end: tuple):
   pass

def convert(ch):
    if ch == 'S':
        return 0
    elif ch == 'E':
        return 27
    else:
        return ord(ch) - 96

def can_move(grid, a, b):
    if grid[b[1],b[0]] - grid[a[1],a[0]] <= 1:
        return True
    return False

def parse_data(path):
    with open(path, 'r', encoding='utf-8') as fp:
        data = fp.read().strip().split('\n')
    x = len(data[0])
    y = len(data)
    grid = np.zeros((y,x), dtype=int)

    for idx, line in enumerate(data):
        grid[idx,:] = np.array([convert(v) for v in line])
    a = np.where(grid == 0)
    start = next(zip(a[0],a[1]))

    a = np.where(grid == 27)
    end = next(zip(a[0],a[1]))

    print(start)
    print(end)
    return grid, start, end

def run(path):
    data, start, end = parse_data(f"{path}/input")

    p1 = None
    p2 = None

    return (p1, p2)

