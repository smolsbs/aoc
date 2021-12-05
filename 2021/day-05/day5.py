#!/usr/bin/env python3

import aocUtils
import numpy as np
from itertools import combinations
from re import search

PAT = r'(\d+),(\d+) -> (\d+),(\d+)'

def grid_size(_points):
    xx, yy = set(), set()
    for p in _points:
        xx.add(p[0][0])
        xx.add(p[1][0])
        yy.add(p[0][1])
        yy.add(p[1][1])
    return (min(xx), min(yy), max(xx), max(yy))

# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
def check_intersect(seg_1, seg_2): 
    x1, x2 = seg_1[0]
    y1, y2 = seg_1[1]
    x3, x4 = seg_2[0]
    y3, y4 = seg_2[1]
    
    t = ((x1 - x3)*(y3 - y4) - (y1-y3)*(x3-x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    u = ((x1 - x3)*(y1 - y2) - (y1-y3)*(x1-x2)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    if t >= 0 and t <= 1 and u >= 0 and u <= 1:
        px = x1 + t*(x2-x1)
        py = y1 + t*(y2-y1)
        print(f'seg1:{seg_1}\tseg_2_:{seg_2}')
        print(f'intersects at {round(px, 1)}, {round(py, 1)}\n')

def make_grid(dataset, lims):
    grid = np.zeros(lims, dtype=np.int8)

    for seg in dataset:
        x1, y1 = seg[0]
        x2, y2 = seg[1]

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                grid[y, x1] += 1
                
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                grid[y1, x] += 1
    n = np.count_nonzero(grid > 1)
    return n



def main():
    data = aocUtils.loadInput('input')
    lines = []
    p1_lines = []

    for p in data:
        x1, y1, x2, y2 = list(map(int, list(search(PAT, p).groups())))
        lines.append([(x1, y1), (x2, y2)])
        if x1 == x2 or y1 == y2:
            p1_lines.append([(x1, y1), (x2, y2)])


    xmin, ymin, xmax, ymax = grid_size(p1_lines)

    p1 = make_grid(p1_lines, (ymax+1,xmax+1))
    # p2 = make_grid(lines, (ymax+1,xmax+1), True)

    print(f'part 1: {p1}')
    # print(f'part 2: {p2}')

if __name__ == '__main__':
    main()