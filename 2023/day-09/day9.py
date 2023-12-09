#!/usr/bin/env python3

import aocUtils
from re import findall

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    return crawl(data)


def crawl(data: list[str]) -> tuple[int, int]:
    p1, p2 = (0,0)

    for line in data:
        nums = list(map(int, findall(r"-?\d+", line)))
        v = get_v(nums)
        p1 += v[0]
        p2 += v[1]

    return (p1,p2)


def get_v(nums: list[int]) -> tuple[int,int]:
    diffs = []
    for i in range(len(nums)-1):
        diffs.append(nums[i+1]-nums[i])

    if all(v == 0 for v in diffs):
        return (nums[-1], nums[0])
    else:
        v = get_v(diffs)
        return (nums[-1] + v[0], nums[0] - v[1])


# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    v = crawl(data)
    assert v[0] == 114

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    v = crawl(data)
    assert v[1] == 2
