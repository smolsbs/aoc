#!/usr/bin/env python3

import aocUtils
from itertools import product

NEIGHBOURS = {(-1,0), (1,0), (0,-1), (0,1)}


def search(origin, grid, part2=False) -> int:

    # point -> tuple[x:int, y:int] 

    mx = len(grid[0])
    my = len(grid)

    toVisit = [origin]
    visited = set()
    
    paths = 0

    while len(toVisit) != 0:
        aux = toVisit.pop()
        visited.add(aux)

        if grid[aux[1]][aux[0]] == 9:
            paths += 1
            continue

        for a,b in NEIGHBOURS:
            point = (aux[0]+a, aux[1]+b)

            if point in visited and not part2:
                continue

            if point[0] < 0 or point[0] >= mx or point[1] < 0 or point[1] >= my:
                continue
            
            if grid[aux[1]][aux[0]] == grid[point[1]][point[0]] - 1:
                toVisit.append(point)

    
    return paths

def parse(data):
    grid = []
    zeros = set()

    for idy, line in enumerate(data):
        aux = []
        for idx, v in enumerate(line):
            v = int(v)
            if v == 0:
                zeros.add((idx,idy))
            aux.append(v)
        grid.append(aux)

    return grid, zeros

def part1(grid, zeros):
    trails = 0
    for zero in zeros:
        trails += search(zero, grid)

    return trails

def part2(grid, zeros):
    trails = 0
    for zero in zeros:
        trails += search(zero, grid, True)

    return trails

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    grid, zeros = parse(data)

    p1 = part1(grid, zeros)
    p2 = part2(grid, zeros)

    return (p1, p2)

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    grid, zeros = parse(data)
    assert part1(grid, zeros) == 36

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    grid, zeros = parse(data)
    assert part2(grid, zeros) == 81
