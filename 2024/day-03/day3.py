#!/usr/bin/env python3

import aocUtils
import re


PATT = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
DONTS = re.compile(r"don\'t\(\)")
DOS = re.compile(r"do\(\)")

def parse_mul(text:str):
    return PATT.findall(text)


def part1(data):
    program_mem = "".join(data)
    _sum = sum(int(v[0])*int(v[1]) for v in parse_mul(program_mem))
    return _sum


def part2(data):
    program_mem = "".join(data)
    
    donts = [(False,v.start()) for v in DONTS.finditer(program_mem)]
    dos = [(True,v.end()) for v in DOS.finditer(program_mem)]
    merged = sorted(donts + dos, key=lambda x: x[1])

    idx = 0
    enabled = True
    new_string = ""

    for point in merged:
        if point[0] is False and enabled:
            new_string += program_mem[idx:point[1]]
            enabled = False

        elif point[0] is True and not enabled:
            enabled = True
            idx = point[1]

    if enabled:
            new_string += program_mem[idx:]

    _sum = sum(int(v[0])*int(v[1]) for v in parse_mul(new_string))

    return _sum



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
    assert part1(data) == 161

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput2")
    assert part2(data) == 49
