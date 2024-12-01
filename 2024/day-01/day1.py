#!/usr/bin/env python3
import collections
import aocUtils


def get_lists(data):
    left, right = [], []
    for line in data:
        a, b = line.split("  ")
        left.append(int(a))
        right.append(int(b))

    return left, right


def part1(data):
    l, r = get_lists(data)

    l = sorted(l)
    r = sorted(r)
    _s = 0

    for i, j in zip(l, r):
        _s += abs(i-j)

    return _s


def part2(data):
    l, r = get_lists(data)
    r_count = collections.Counter(r)

    _s = 0
    for j in l:
        if j not in r_count.keys():
            continue

        _s += j * r_count[j]

    return _s


def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    p1 = part1(data)
    p2 = part2(data)

    return (p1, p2)

# === Testing suite ===


def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute()


def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    assert part1(data) == 11


def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    assert part2(data) == 31
