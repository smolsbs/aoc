#!/usr/bin/env python3

import aocUtils

def get_priority(ch):
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
        return ord(ch) - 96
    return ord(ch) - 64 + 26


def solve_part_1(data):
    priorities = 0
    for line in data:
        half = len(line) // 2
        p1 = set(line[:half])
        p2 = set(line[half:])

        v = p1.intersection(p2).pop()
        priorities += get_priority(v)
    return priorities

def solve_part_2(data):
    p = 0
    for i in range(0, len(data), 3):
        chars = set(data[i])
        chars = chars.intersection(set(data[i+1]))
        chars = chars.intersection(set(data[i+2]))

        p += get_priority(chars.pop())

    return p


def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    p1 = solve_part_1(data)
    p2 = solve_part_2(data)

    return p1, p2
