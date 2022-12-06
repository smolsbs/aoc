#!/usr/bin/env python3

from collections import defaultdict
from re import findall
import copy

import aocUtils

def solve_part_1(crates, moves):
    for move in moves:
        p, a, b = map(int, findall("\d+", move))

        for _ in range(p):
            crates[b].append(crates[a].pop())

    part1 = ""
    for i in range(1, len(crates)+1):
        part1 += crates[i][-1]
    return part1

def solve_part_2(crates, moves):
    for move in moves:
        p, a, b = map(int, findall("\d+", move))
        crates[b] += crates[a][-p:]

        for _ in range(p):
            crates[a].pop()
    
    part2 = ""
    for i in range(1, len(crates)+1):
        part2 += crates[i][-1]
    return part2

def create_crates(data):
    crates = defaultdict(list)
    max_n = int(max(findall((r"\d"), data[0])))

    for l in data[1:]:
        i = 1
        while i <= max_n:
            pos = -3 + 4*i
            if l[pos] != " ":
                crates[i].append(l[pos])
            i += 1
    
    return crates

def loadInput(_path):
    fp = open(_path, 'r')
    lines = fp.read().split('\n')
    if lines[-1] == "":
        lines.pop()
    fp.close()
    
    for l, idx in zip(lines, range(len(lines))):
        if l == '':
            lines.pop(idx)
            crates = create_crates(lines[idx-1::-1])
            moves = lines[idx:]
            break
    
    return dict(crates), moves

def run(path):

    crates, moves = loadInput(f"{path}/input")

    p1 = solve_part_1(copy.deepcopy(crates), moves)
    p2 = solve_part_2(copy.deepcopy(crates), moves)

    return (p1, p2)
