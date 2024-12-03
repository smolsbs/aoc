#!/usr/bin/env python3

import aocUtils
from re import findall

def parse_data(data: list[str]):
    values = []
    for line in data:
        numbs = list(map(int, findall(r"\d+", line)))
        values.append([numbs, check_valid(numbs)])

    return values

def check_valid(numbers) -> list[int]:
    faults = []

    signs = sum([numbers[i-1]-numbers[i] for i in range(1, len(numbers))])

    if signs < 0: 
        sign = -1
    else:
        sign = 1

    for i in range(1, len(numbers)):
        v = numbers[i-1] - numbers[i]

        if v == 0 or abs(v) > 3:
            if i == 1:
                faults.append(i-1)
            faults.append(i)

        if (sign == -1 and v > 0) or (sign == 1 and v < 0):
            if i == 1:
                faults.append(i-1)
            faults.append(i)

    return faults

def check_faults(values, faults):
    for fault in faults:
        aux = [v for v in values]
        aux.pop(fault)

        if len(check_valid(aux)) == 0:
            return True
    return False

def part1(data: list) -> int:
    return sum(1 if len(v[1]) == 0 else 0 for v in data)

def part2(data: list[str]):
    _s = sum(1 if len(v[1]) == 0 else 0 for v in data)

    for val in data:
        if len(val[1]) == 0:
            continue
        
        if check_faults(val[0], val[1]):
            _s += 1
            continue
    
    return _s




def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    _data = parse_data(data)

    p1 = part1(_data)
    p2 = part2(_data)

    return (p1, p2)

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    _data = parse_data(data)
    assert part1(_data) == 2

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    _data = parse_data(data)
    assert part2(_data) == 4
