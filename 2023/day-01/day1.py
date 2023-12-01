#!/usr/bin/env python3

import aocUtils
from re import finditer

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    p1 = part1(data)
    p2 = part2(data)

    return (p1, p2)


nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
def get_digit(line:str, part2:bool=False) -> list:
    _ret = []
    res = list(finditer(r"\d", line))
    if len(res) == 0:
        pass
    else:
        _ret += [(int(v[0]),v.start()) for v in res]

    if not part2:
        return list(sorted(_ret, key=lambda x:x[1]))

    for idx, v in enumerate(nums):
        res = list(finditer(v,line))
        if len(res) == 0:
            continue
        if len(res) == 1:
            _ret.append((idx,res[0].start()))
        else:
            _ret.append((idx,res[0].start()))
            _ret.append((idx,res[-1].start()))

    return list(sorted(_ret, key=lambda x:x[1]))


def part1(data:list[str]) -> int:
    p1 = 0
    for line in data:
        _ret = get_digit(line)
        p1 +=  10*_ret[0][0] + _ret[-1][0]
    return p1

def part2(data:list[str]) -> int:
    p2 = 0
    for line in data:
        _ret = get_digit(line,True)
        p2 += 10*_ret[0][0] + _ret[-1][0]
    return p2


