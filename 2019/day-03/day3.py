#!/usr/bin/env python3

import AoCUtils
import numpy as np

from collections import defaultdict

def _getPoints(data):
    moveset = {'D':(0,-1), 'U':(0,1), 'L':(-1,0), 'R':(1,0)}
    seq = []
    for line in data:
        seq.append(line.split(','))

    # store every single point where any of the wires pass and it's lenght
    points = defaultdict(lambda: None)

    # iterate over each wire to path out both of them
    for id in range(1, 3):
        (x, y) = 0, 0
        dist = 0
        for act in seq[id-1]:
            (move, amount) = moveset[act[0]], int(act[1:])
            for j in range(amount):
                x += move[0]
                y += move[1]
                dist += 1
                if points[(x,y)] == None:
                    points[(x,y)] = [set(), [], []]
                points[(x,y)][0].add(id)
                points[(x,y)][id].append(dist)
    return points

def manhattan(p1, p2):
    return int(sum(abs(a-b) for a, b in zip(p1, p2)))

def main():
    data = AoCUtils.loadInput('input')

    # get every point
    crossed = _getPoints(data)

    # fitler out the points where only one wire passed through
    same = {k:v[1:] for k,v in crossed.items() if len(v[0]) == 2}
    same_p1 = list(same.keys()) # we only need the points themselves
    same_p2 = {k:(v[0][0], v[1][0]) for k,v in same.items()} # get the first lenght for each wire

    # sort for the cityblock distance and the sum of wire length, respectively 
    p1 = manhattan([0,0],sorted(same_p1, key=lambda x: manhattan([0,0], x))[0])
    p2 = sum(sorted(same_p2.values(), key=lambda x: sum(x))[0])
    print("part1: {}\npart2: {}".format(p1,p2))


if __name__ == '__main__':
    main()
