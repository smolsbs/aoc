#!/usr/bin/env python3

import AoCUtils
import numpy as np

from pprint import pprint
from scipy.spatial.distance import cdist

def lineIntersect(a1, a2, b1, b2):
    # https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect#565282
    r = a1 - a2
    s = b1 - b2
    num = np.cross((b1-a1), r)  # ( q -p ) x r
    denom = np.cross(r, s)      # r x s
    if denom == 0:
        # paralell
        return -1
    t = np.cross((b1-a1), s) / denom
    u = np.cross((b1-a1),r) / denom

    if num == 0 and denom == 0:
        return -1

    if denom != 0 and np.abs(t) <= 1 and np.abs(u) <= 1:
        return list(a1+t*r)
    return -1

def getPoints(seq):
    (x, y) = 0.0, 0.0
    steps = [ [np.array([0.,0.]), 0]]   # store all the points of the wires
    i = 0                               # distance that the wire traveled (for part 2)
    for act in seq:
        (move, amount) = act[0].lower(), int(act[1:])

        if move == 'u':
            y += amount
        elif move == 'd':
            y -= amount
        elif move == 'l':
            x -= amount
        elif move == 'r':
            x += amount
        i += amount
        steps.append(( np.array([x, y]), i ))
        
    return steps

def manhattan(p1, p2):
    return sum(abs(a-b) for a, b in zip(p1, p2))

def main():
    # data = AoCUtils.loadInput('input')
    data = AoCUtils.loadInput('sinput')

    crossed = []
    wire1 = getPoints(data[0].split(','))
    wire2 = getPoints(data[1].split(','))

    # iterate over every pair of segments of wire and find if both intercept. If so,
    # append the resulting point and wire distances to a list

    for i in range(0, len(wire1)-1, 1):
        for j in range(0, len(wire2)-1, 1):
            res = lineIntersect(wire1[i][0], wire1[i+1][0], wire2[j][0], wire2[j+1][0])
            if res != -1:
                crossed.append((res, wire1[i][1], wire2[j][1]))

    p1 = sorted(crossed, key=lambda x: manhattan([0, 0], x[0]))
    p2 = sorted(crossed, key=lambda x: x[1] + x[2])
    print("part 1: {}".format( int(manhattan([0,0], p1[0][0])) ) )
    print("part 2: {}".format(p2[0][1] + p2[0][2]))

    


if __name__ == '__main__':
    main()
