#!/usr/bin/env python3

import aocUtils

DIRS = [(0,-1), (1, 0), (0,1), (-1,0)]


def parse_info(data: list[str])-> tuple[list[list[str]],tuple[int,int]| None]:
    
    grid = []
    init_pos = None

    for yy,line in enumerate(data):
        row = []
        for xx, c in enumerate(line):
            if c == '^':
                init_pos = (xx,yy)
            v = 1 if c == '#' else 0

            row.append(v)

        grid.append(row)
    return grid, init_pos


def check_inbound(pos, max_x, max_y)-> bool:
    if (pos[0] >= 0 and pos[0] < max_y) and (pos[1] >= 0 and pos[1] < max_x):
        return True
    return False


def solve(grid, pos):
    MAX_STEPS = 100000

    idx = 0
    move_idx = 0
    seen = set()
    curr_pos = pos

    max_x = len(grid[0])
    max_y = len(grid)

    while True and idx < MAX_STEPS:
        idx += 1
        seen.add(curr_pos)

        next_pos = (curr_pos[0] + DIRS[move_idx][0], curr_pos[1] + DIRS[move_idx][1])

        if not check_inbound(next_pos, max_x, max_y):
            break

        if grid[next_pos[1]][next_pos[0]] == 1:
            move_idx = (move_idx + 1) % 4
            continue
        
        curr_pos = next_pos
        
    
    # extra(grid, seen)
    if idx >= MAX_STEPS:
        return []
    return seen

def part1(grid, init_pos) -> int:
    
    return len(solve(grid, init_pos))



def extra(grid, seen):
    from PIL import Image, ImageDraw
    a = Image.new("RGB", (130,130))
    d = ImageDraw.Draw(a)
    d.point(list(seen), fill=(0,255,00))
    for yy in range(len(grid)):
        for xx in range(len(grid[yy])):

            if grid[yy][xx] == 1:
                d.point((xx,yy), fill=(255,0,0))
                
    a = a.resize((130*4, 130*4), Image.Resampling.NEAREST)
    a.save("amatsugu.png")



def part2(grid, player, seen_p1):
    # bruteforcing the part2 by putting an obstacle
    # on every position the guard took for part1
    # and checking if solve() passes the MAX_STEPS
    # if yes, that means we're probably in a loop
    nice = 0

    for c in seen_p1:
        grid[c[1]][c[0]] = 1
        
        a = solve(grid, player)

        if len(a) == 0:
            nice += 1

        grid[c[1]][c[0]] = 0

    return nice



def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    grid, player = parse_info(data)
    p1 = part1(grid, player)
    seen = solve(grid, player)
    p2 = part2(grid, player, seen)

    return (p1, p2)

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    grid, player = parse_info(data)
    assert part1(grid, player) == 41

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    grid, player = parse_info(data)
    seen = solve(grid, player)
    assert part2(grid, player, seen) == 6
    
