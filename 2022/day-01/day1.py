#!/usr/bin/env python3

from collections import deque
import aocUtils

def run(path):
    cals = list()
    fp = open(f"{path}/input", 'r')

    c = 0
    for line in fp.read().split('\n'):
        if line != "":
            c += int(line)
        else:
            cals.append(c)
            c = 0
    fp.close()
    
    cals = sorted(cals, reverse=True)[:3]
    p1 = cals[0]
    p2 = sum(cals)

    print(f'part1: {p1}')
    print(f'part2: {p2}')

