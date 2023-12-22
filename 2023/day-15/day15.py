#!/usr/bin/env python3

import aocUtils

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    p1, p2 = parse(data[0])

    return (p1, p2)


def parse(data:str) -> tuple[int,int]:
    _sum = 0
    boxes = [[] for _ in range(256)]
    for code in data.split(','):
        v = calc_HASH(code)
        
        _id, strength = get_id(code)
        box_id = calc_HASH(_id)

        if strength == -1:
            rem_from_box(boxes, box_id, _id)
        else:
            add_to_box(boxes, box_id, _id, strength)

        _sum += v

    p2 = get_focusing_power(boxes)
    return (_sum, p2) 

def rem_from_box(boxes: list[list[tuple[str,int]]], bId: int, code: str) -> None:
    aux = -1
    for idx in range(len(boxes[bId])):
        if boxes[bId][idx][0] == code:
            aux = idx
            break
    
    if aux != -1:
        boxes[bId].pop(aux)

def add_to_box(boxes: list[list[tuple[str,int]]], bId: int, code: str, val: int) -> None:
    aux = -1
    for idx in range(len(boxes[bId])):
        if boxes[bId][idx][0] == code:
            aux = idx
            break

    if aux != -1:
        boxes[bId][aux] = (code, val)
    else:
        boxes[bId].append((code,val))


def get_focusing_power(boxes: list[list[tuple[str,int]]]) -> int:
    _sum = 0
    for bId, box in enumerate(boxes):
        for lId, lens in enumerate(box):
            _sum += (bId+1)*(lId+1)*lens[1]

    return _sum

def get_id(code: str) -> tuple[str,int]:
    _id = ""
    val = -1
    for idx,c in enumerate(code):
        if c == '=':
            val = int(code[idx+1])
            break
        if c == '-':
            break
        _id += c

    return (_id, val)

def calc_HASH(code: str) -> int:
    currVal = 0
    for c in code:
        currVal += ord(c)
        currVal *= 17
        currVal %= 256

    return currVal

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    v = parse(data[0])[0]

    assert v == 1320

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    v = parse(data[0])[1]

    assert v == 145
