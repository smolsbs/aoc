#!/usr/bin/env python3

import aocUtils
from itertools import product

COORDS = [v for v in product([-1,0,1], repeat=2) if v != (0,0)]



def make_grid(lines: list[str]) -> tuple[list[list[str]], int, int]:
    grid = [[c for c in line] for line in lines]
    return (grid, len(grid), len(grid[0]))


def get_x(grid, pos_x, pos_y, max_x, max_y) -> int:

    w = ["" for _ in range(2)]

    vert_bound = pos_y > 0 and pos_y < max_y-1
    horiz_bound = pos_x > 0 and pos_x < max_x - 1
    
    if vert_bound and horiz_bound:
        w[0] = f"{grid[pos_y-1][pos_x-1]}A{grid[pos_y+1][pos_x+1]}"
        w[1] = f"{grid[pos_y-1][pos_x+1]}A{grid[pos_y+1][pos_x-1]}"

    if w[0] in {"MAS", "SAM"} and w[1] in {"MAS", "SAM"}:
        return 1
    return 0




def get_words(grid, pos_x, pos_y, max_x, max_y) -> int:
    words = ["X" for _ in range(len(COORDS))]
    for i in range(1,4):
        for idx,c in enumerate(COORDS):
            x = pos_x + i*c[0]
            y = pos_y + i*c[1]

            if (x >= 0 and x < max_x) and (y >= 0 and y < max_y):
                words[idx] += grid[y][x]

    return sum([1 if v == "XMAS" else 0 for v in words])


def part1(grid, max_x, max_y):
    _sum = 0

    for yy in range(0, max_y):
        for xx in range(0, max_x):

            if grid[yy][xx] != 'X':
                continue

            _sum += get_words(grid, xx, yy, max_x, max_y)

    return _sum

def part2(grid, max_x, max_y):
    _sum = 0

    for yy in range(0, max_y):
        for xx in range(0, max_x):

            if grid[yy][xx] != 'A':
                continue

            _sum += get_x(grid, xx, yy, max_x, max_y)

    return _sum


def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    grid, max_x, max_y = make_grid(data)

    p1 = part1(grid, max_x, max_y)
    p2 = part2(grid, max_x, max_y)

    return (p1, p2)

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    grid, m_x, m_y = make_grid(data)
    assert part1(grid, m_x, m_y) == 18

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    grid, m_x, m_y = make_grid(data)
    assert part2(grid, m_x, m_y) == 9
