#!/usr/bin/env python3

def solve(data):
    p1 = None
    p2 = None

    for idx in range(4, len(data)):
        if len(set(data[idx-4:idx])) == 4 and not p1:
            p1 = idx
        if idx < 14:
            continue
        if len(set(data[idx-14:idx])) == 14 and not p2:
            p2 = idx
        if p1 and p2:
            break

    return p1, p2

def run(path):
    with open(f'{path}/input', 'r') as fp:
        data = fp.read().strip('\n')

    return solve(data)
