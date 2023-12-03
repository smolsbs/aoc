#!/usr/bin/env python3

import aocUtils
from re import finditer
import string


SYMBOLS = set(string.punctuation) - {'.'}

def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    info = crawl_grid(data)

    p1 = sum([sum(v) for v in list(zip(*info))[1]])
    p2 = get_gear_ratio(info)

    return (p1, p2)


def crawl_grid(data: list[str]) -> list[tuple[str, list[int]]]:
    nList = get_all_nums(data)
    found_numbers = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] in SYMBOLS:
                aux = find_numbers(data, nList, x, y)
                if len(aux) == 0:
                    continue
                found_numbers.append((data[y][x], aux))
    return found_numbers
            

def get_all_nums(data: list[str]) -> list[list[tuple[int,int,int]]]:
    list_of_n = []
    for line in data:
        line_of_n = []
        for n in finditer(r"\d+", line):
            # (number, startpos on string, endpos on string)
            line_of_n.append((int(n.group(0)), n.start(), n.end()-1))
        list_of_n.append(line_of_n)
    return list_of_n


def find_numbers(data, nList, x,y) -> list[int]:
    numbers = []
    for i in range(-1, 2):
        yy = y+i
        if yy < 0 or yy == len(data):
            continue
        if len(nList[yy]) == 0:
            continue
        for val in nList[yy]:
            if val[2] < x-1:
                continue
            if val[1] > x+1:
                continue
            numbers.append(val[0])

    return numbers


def get_gear_ratio(found_numbers: list[tuple[str, list[int]]]) -> int:
    val = 0
    for gear in found_numbers:
        if gear[0] != '*':
            continue
        if len(gear[1]) != 2:
            continue
        val += gear[1][0]*gear[1][1]

    return val


# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    info = crawl_grid(data)
    value = sum([ sum(v) for v in list(zip(*info))[1]])
    assert value == 4361
    
def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    v = crawl_grid(data)
    assert get_gear_ratio(v) == 467835
