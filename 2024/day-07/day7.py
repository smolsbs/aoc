#!/usr/bin/env python3

import aocUtils
from operator import mul, add
from itertools import product
from re import findall


def concat(a,b):
    return int(f"{a}{b}")

OPS = [mul, add, concat]

def apply_operations(n, r):
    s = n.pop(0)

    for idx in range(len(n)):
        s = OPS[r[idx]](s,n[idx])

    return s


def rec(tot, n, _r=2):
    ways = list(product(range(_r), repeat=len(n)-1))

    for way in ways:
        _values = [ v for v in n]
        if apply_operations(_values, way ) == tot:
            return tot

    return 0

def parse(data):
    values = []

    for d in data:
        aux = list(map(int,findall(r"\d+",d)))
        values.append((aux[0], aux[1:]))
    
    return values


def part1(values):
    s = 0
    for t, n in values:
        s += rec(t,n)
    return s


def part2(values):
    s = 0
    for t, n in values:
        s += rec(t,n,3)
    return s

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    values = parse(data)

    p1 = part1(values)
    p2 = part2(values)

    return (p1, p2)

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    aux = parse(data)
    assert part1(aux) == 3749

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    aux = parse(data)
    assert part2(aux) == 11387
