#!/usr/bin/env python3

import aocUtils
import numpy as np


def can_move(grid, currNode, nextNode):
    if grid[currNode[0],currNode[1]] - grid[nextNode[0],nextNode[1]] <= 1:
        return 1
    return 10**10

def convert(ch):
    if ch == 'S':
        return 0
    elif ch == 'E':
        return 27
    else:
        return ord(ch) - 96

def get_neighbours(y,x, max_y, max_x):
    aux = []
    # left
    if x != 0:
        aux.append((y,x-1))
    # right
    if x != max_x-1:
        aux.append((y,x+1))
    # up
    if y != 0:
        aux.append((y-1,x))
    # down
    if y != max_y-1:
        aux.append((y+1,x))
    return aux

def is_b(grid, node):
    return grid[node[0],node[1]] == 2
        
def get_lowest(_dict:dict) -> dict:
    return sorted(_dict.items(), key=lambda x: x[1]['dist'])[0][1]

def pathfind(grid, start, end):
    max_y, max_x = np.shape(grid)
    unvisited = {}
    visited = {}
    for r in range(max_y):
        for c in range(max_x):
            unvisited[(r, c)] = {'from': None, 'dist': 10**9, 'coords': (r,c)}

    unvisited[(start[0],start[1])]['dist'] = 0     

    while len(unvisited) > 0:
        currNode = get_lowest(unvisited)
        y,x = currNode['coords']
        visited[currNode['coords']] = currNode
        del(unvisited[(y,x)])
        if (y,x) == end:
            break

        for yx in get_neighbours(y, x, max_y, max_x):
            if yx in visited.keys():
                continue

            cost = can_move(grid, yx, currNode['coords']) + currNode['dist']
            if cost < unvisited[yx]['dist']:
                unvisited[yx]['dist'] = cost
                unvisited[yx]['from'] = currNode['coords']

    return visited[end]['dist']

def solve_part_1(grid:np.ndarray, start: tuple, end: tuple) -> int:
    return pathfind(grid, start, end)

def solve_part_2(grid:np.ndarray, end: tuple):
    max_y, max_x = np.shape(grid)
    list_of_a = np.where(grid == 1)
    candidates = set()
    for yx in zip(list_of_a[0],list_of_a[1]):
        viz = get_neighbours(yx[0], yx[1], max_y, max_x)
        for n in viz:
            if is_b(grid, n):
                candidates.add(yx)
                break
    
    p2 = 10**9
    for candidate in candidates:
        print(f"Trying {candidate}")
        v = pathfind(grid, candidate, end)

        if v < p2:
            p2 = v

    return p2


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

    return grid, start, end

def run(path):
    data, start, end = parse_data(f"{path}/input")

    p1 = solve_part_1(data, start, end)
    p2 = solve_part_2(data, end)

    return (p1, p2)

