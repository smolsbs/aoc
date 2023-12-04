#!/usr/bin/env python3

import aocUtils
from re import findall
from collections import defaultdict

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    return get_points(data)

def get_points(data:list[str]) -> tuple[int,int]:
    scorecards = defaultdict(int)
    pts = 0

    for idx, line in enumerate(data):
        str_card,str_usrNums = line.split(" | ")

        aux = map(int, findall(r"\d+", str_card))
        next(aux)
        card = set(aux)
        usrNums = set(map(int, findall(r"\d+", str_usrNums)))

        inNums =len(card.intersection(usrNums))
        scorecards[idx+1] += 1
        if inNums == 0:
            continue

        dupes = scorecards[idx+1]
        for i in range(1, inNums+1):
            scorecards[idx+i+1] += dupes

        pts += 2 ** (inNums - 1)

    return (pts, sum(scorecards.values())) 


# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    assert get_points(data)[0] == 13

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    assert get_points(data)[1] == 30
