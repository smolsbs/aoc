#!/usr/bin/env python3

import numpy as np
import aocUtils

def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    grid = parse_data(data)
    points = check_empty_lines(grid)
    points_p2 = check_empty_lines(grid, 10**6 - 1)

    p1 = get_shortest_pairs(points)
    p2 = get_shortest_pairs(points_p2)

    return (p1, p2)

def parse_data(data: list[str]) -> np.ndarray:
    r = len(data)
    c = len(data[0])
    grid = np.ndarray(shape=(r,c), dtype=np.int32)
    for idx, l in enumerate(data):
        grid[idx, :] = np.array([0 if c == '.' else 1 for c in l])

    return grid

def check_empty_lines(grid: np.ndarray, expand:int=1) -> list[tuple[int,int]]:
    r,c = grid.shape

    r_expand = []
    c_expand = []

    for idx in range(r):
        a = grid[idx, :]
        v = not a.any()
        if v:
            r_expand.append(idx)

    for idx in range(c):
        a = grid[:, idx]
        v = not a.any()
        if v:
            c_expand.append(idx)
    
    points = find_points(grid)
    
    # row
    for idx, pt in enumerate(points):
        r,c = pt
        new_r, new_c = pt 
        for e in r_expand:
            if r < e:
                continue
            new_r += expand

        for e in c_expand:
            if c < e:
                continue
            new_c += expand
        points[idx] = (new_r, new_c)

    return points

def find_points(grid: np.ndarray) -> list[tuple[int,int]]:
    return list(zip(*np.where(grid == 1)))


def get_shortest_pairs(points:list[tuple[int, int]]) -> int:
    _sum = 0
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            a = abs(points[i][0]-points[j][0])
            b = abs(points[i][1]-points[j][1])
            _sum += a+b
    return _sum

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    grid = parse_data(data)
    points = check_empty_lines(grid)

    assert get_shortest_pairs(points) == 374

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    grid = parse_data(data)
    pts_10 = check_empty_lines(grid, 9)
    pts_100 = check_empty_lines(grid, 99)

    assert get_shortest_pairs(pts_10) == 1030
    assert get_shortest_pairs(pts_100) == 8410

