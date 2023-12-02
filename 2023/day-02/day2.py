#!/usr/bin/env python3

from collections.abc import Generator
from typing import Any
import aocUtils


RED = 12
GREEN = 13
BLUE = 14

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    aux = [(a,b) for a,b in check_games(data)]

    p1 = sum(list(zip(*aux))[0])
    p2 = sum(list(zip(*aux))[1])

    return (p1, p2)

def check_games(game_list:list[str]) -> Generator[tuple[int,int], Any, Any]:
    for game in game_list:
        id, sets = game.split(": ")
        id = int(id.split(" ")[1])
        v, n = check_sets(sets)
        if v:
            yield (id, n)
        else:
            yield (0, n)

def check_sets(sets:str) -> tuple[bool,int]:
    r,g,b = (0,0,0)
    valid = True
    for _set in sets.split("; "):
        # part 1
        if valid:
            valid = check_valid_hand(_set)

        # part 2
        rgb = check_dices(_set)
        if rgb[0] > r:
            r = rgb[0]
        if rgb[1] > g:
            g = rgb[1]
        if rgb[2] > b:
            b = rgb[2]
    return (valid, r*g*b)

def check_dices(_set:str) -> tuple[int,int,int]:
    aux = _set.split(", ")
    r,g,b = (0,0,0)
    for dice in aux:
        n, c = dice.split(" ")
        n = int(n)
        if c[0] == 'r' and n > r:
            r = n
        elif c[0] == 'g' and n > g:
            g = n
        elif c[0] == 'b' and n > b:
            b = n
    return (r,g,b)

def check_valid_hand(_set:str) -> bool:
    aux = _set.split(", ")
    for dice in aux:
        n, c = dice.split(" ")
        n = int(n)
        if c[0] == 'r' and n > RED:
            return False
        elif c[0] == 'g' and n > GREEN:
            return False
        elif c[0] == 'b' and n > BLUE:
            return False
    return True


# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    _ret = [ v for v,_ in check_games(data)]
    assert sum(_ret) == 8

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    _ret = [ v for _,v in check_games(data)]
    assert sum(_ret) == 2286
