#!/usr/bin/env python3

import aocUtils
from re import findall

def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    v = thing(data)

    p1 = sorted(v)[0]
    p2 = None

    return (p1, p2)


def thing(data):
    seed_to_soil = list()
    soil_to_fert = list()
    fert_to_water = list()
    water_to_light = list()
    light_to_temp = list()
    temp_to_hum = list()
    hum_to_loc = list()

    seeds = list(map(int, findall(r"\d+", data[0])))
    
    idx = 3
    # seed to soil
    while data[idx] != '':
        seed_to_soil.append(parser(data[idx]))
        idx += 1

    # soil to fert
    idx += 2
    while data[idx] != '':
        soil_to_fert.append(parser(data[idx]))
        idx += 1

    #fert to water
    idx += 2
    while data[idx] != '':
        fert_to_water.append(parser(data[idx]))
        idx += 1

    # water to light
    idx += 2
    while data[idx] != '':
        water_to_light.append(parser(data[idx]))
        idx += 1
    
    # light to temp
    idx += 2
    while data[idx] != '':
        light_to_temp.append(parser(data[idx]))
        idx += 1

    # temp to hum
    idx += 2
    while data[idx] != '':
        temp_to_hum.append(parser(data[idx]))
        idx += 1

    # hum to loc
    idx += 2
    while idx < len(data):
        hum_to_loc.append(parser(data[idx]))
        idx += 1

    seed_to_loc = set()
    for s in seeds:
        a = a_to_b(s, seed_to_soil)
        b = a_to_b(a, soil_to_fert)
        c = a_to_b(b, fert_to_water)
        d = a_to_b(c, water_to_light)
        e = a_to_b(d, light_to_temp)
        f = a_to_b(e, temp_to_hum)
        seed_to_loc.add(a_to_b(f, hum_to_loc))

    
    return seed_to_loc

def a_to_b(id, mapper):
    for m in mapper:
        s,d,r = m
        if id < d:
            continue
        if id > d+r:
            continue
        return s+(id-d)
    return id


def parser(line:str):
    s, d, r = list(map(int, findall(r"\d+", line)))
    return (s,d,r)


# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    v = thing(data)

    assert sorted(v)[0] == 35

def test_p2():
    assert None == 46


