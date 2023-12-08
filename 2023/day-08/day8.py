#!/usr/bin/env python3

import aocUtils
from math import gcd
from re import findall

def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    steps, nodes = parse_data(data)
    p2_nodes = get_cycle(steps, nodes)

    p1 = crawl(steps, nodes)
    p2 = get_lcm_all(p2_nodes)

    return (p1, p2)

def parse_data(data: list[str]) -> tuple[list[str],dict]:
    steps = list(data[0])
    nodes = dict()

    for l in data[2:]:
        aux = findall(r"\w+", l)
        nodes[aux[0]] = (aux[1], aux[2])

    return steps, nodes

def crawl(steps: list[str], nodes: dict) -> int:
    count = 0

    currNode = "AAA"
    idx = 0
    size_nodes = len(steps)
    while currNode != "ZZZ":
        turn = steps[idx % size_nodes]

        if turn == 'L':
            currNode = nodes[currNode][0]
        else:
            currNode = nodes[currNode][1]
        
        idx += 1
        count += 1

    return count

def get_cycle(steps: list[str], nodes: dict) -> list[int]:
    counter = 0
    idx = 0

    starting_nodes = list(filter(lambda x: x.endswith('A'), nodes.keys()))
    steps_size = len(steps)
    cycles = []

    while len(starting_nodes) != 0:
        to_del = set()
        turn = steps[idx % steps_size]
        for node_idx in range(len(starting_nodes)):
            if starting_nodes[node_idx].endswith('Z'):
                to_del.add(starting_nodes[node_idx])
                cycles.append(counter)
                continue

            node = starting_nodes[node_idx]

            if turn == 'L':
                starting_nodes[node_idx] = nodes[node][0]
            else:
                starting_nodes[node_idx] = nodes[node][1]
        
        idx += 1
        counter += 1
        if len(to_del) != 0:
            for i in to_del:
                starting_nodes.remove(i)
            
    return cycles


def get_lcm_all(numbers: list[int]) -> int:
    a = numbers[0]
    for v in numbers[1:]:
        b = v
        a = lcm(a,b)

    return a

def lcm(a: int,b: int) -> int:
    return a*b // gcd(a,b)


# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput")
    s, n = parse_data(data)
    v = crawl(s,n)
    assert v == 2

def test_p2():
    data = aocUtils.loadInput(f"{get_sinput_path()}/sinput2")
    s, n = parse_data(data)
    v = get_cycle(s,n)
    l = get_lcm_all(v)
    assert l == 6
