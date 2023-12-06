#!/usr/bin/env python3

import aocUtils
from re import findall

def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    
    parsed_data = get_time_and_dist(data)
    p1 = run_races(parsed_data)

    parsed_data_p2 = parse_p2(data)
    p2 = calculate_range(parsed_data_p2)

    return (p1, p2)

def run_races(races: list[tuple[int,int]]) -> int:
    v = 1
    for race in races:
        v *= calculate_range(race)
    return v

def calculate_range(race: tuple[int,int]) -> int:
    sPos = find_start(race)
    ePos = race[0] - sPos
    return ePos - sPos + 1


def find_start(values:tuple[int,int]) -> int:
    sPos = 0
    max_t, dist = values
    for i in range(dist//max_t, max_t//2):
        run_dist = i * (max_t-i)
        if run_dist > dist:
            sPos = i
            break
    return sPos

def parse_p2(data: list[str]) -> tuple[int,int]:
    time =int(data[0].split(":")[1].replace(" ", ""))
    dist =int(data[1].split(":")[1].replace(" ", ""))

    return (time,dist)

def get_time_and_dist(data:list[str]) -> list[tuple[int,int]]:
    time = list(map(int, findall(r"\d+", data[0])))
    dist = list(map(int, findall(r"\d+", data[1])))

    return list(zip(time, dist))

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    t = get_time_and_dist(data)
    assert run_races(t) == 288

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    v = parse_p2(data)
    assert calculate_range(v) == 71503
