#!/usr/bin/env python3

import aocUtils
from re import findall

PAT = r"(\d+)-(\d+),(\d+)-(\d+)"


def solve(data):
    fully_contained = 0
    contained = 0
    for line in data:
        b1,e1,b2,e2 = map(int, findall(PAT, line)[0])

        elf1 = set(range(b1,e1+1))
        elf2 = set(range(b2, e2+1))
        
        combined = elf1.union(elf2)

        # p1
        if len(combined) == max(map(len, (elf1, elf2))):
            fully_contained += 1

        # p2
        if len(combined) != (len(elf1) +  len(elf2)):
            contained += 1

    return fully_contained, contained

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    p1, p2 = solve(data)

    return (p1, p2)

