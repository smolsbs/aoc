#!/usr/bin/env python3

import aocUtils


from collections import defaultdict
from itertools import combinations


def parse(data):
    max_X = len(data[0])
    max_Y = len(data)

    nodes = defaultdict(list)

    for yy in range(max_Y):
        for xx in range(max_X):
            if data[yy][xx] == ".":
                continue

            f = data[yy][xx]

            nodes[f].append((xx, yy))

    return nodes


def bound_check(p, xx, yy):
    x = p[0] >= 0 and p[0] < xx
    y = p[1] >= 0 and p[1] < yy

    return x and y


def create_p2_antinodes(pos, xx, yy):
    anti = set()

    for c in combinations(pos, 2):
        n1, n2 = c

        # add nodes since they're antinodes as well
        anti.add(n1)
        anti.add(n2)

        vx = n2[0] - n1[0]
        vy = n2[1] - n1[1]


        a1 = (n1[0] - vx, n1[1] - vy)
        while bound_check(a1, xx, yy):
            anti.add(a1)
            a1 = (a1[0] - vx, a1[1] - vy)

        a2 = (n2[0] + vx, n2[1] + vy)
        while bound_check(a2, xx, yy):
            anti.add(a2)
            a2 = (a2[0] + vx, a2[1] + vy)


    return anti


def create_antinodes(pos, xx, yy):
    anti = set()

    for c in combinations(pos, 2):
        n1, n2 = c

        vx = n2[0] - n1[0]
        vy = n2[1] - n1[1]

        a1 = (n1[0] - vx, n1[1] - vy)
        a2 = (n2[0] + vx, n2[1] + vy)

        if bound_check(a1, xx, yy):
            anti.add(a1)
        if bound_check(a2, xx, yy):
            anti.add(a2)

    return anti


def part1(nodes, max_x, max_y):
    antinodes = set()

    for pos in nodes.values():
        antinodes = antinodes.union(create_antinodes(pos, max_x, max_y))

    return len(antinodes)

def part2(nodes, max_x, max_y):
    antinodes = set()

    for pos in nodes.values():
        antinodes = antinodes.union(create_p2_antinodes(pos, max_x, max_y))


    return len(antinodes)

def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    max_X = len(data[0])
    max_Y = len(data)
    nodes = parse(data)

    p1 = part1(nodes, max_X, max_Y)
    p2 = part2(nodes, max_X, max_Y)

    return (p1, p2)


# === Testing suite ===
def get_sinput_path():
    from pathlib import Path

    return Path(__file__).parent.absolute()


def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    max_X = len(data[0])
    max_Y = len(data)

    aux = parse(data)

    assert part1(aux, max_X, max_Y) == 14


def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    max_X = len(data[0])
    max_Y = len(data)

    aux = parse(data)
    assert part2(aux, max_X, max_Y) == 34
