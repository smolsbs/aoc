#!/usr/bin/env python3

def run(path):
    cals = list()
    fp = open(f"{path}/input", 'r')

    c = 0
    for line in fp.read().split('\n'):
        if line != "":
            c += int(line)
        else:
            cals.append(c)
            c = 0
    fp.close()

    cals = sorted(cals, reverse=True)[:3]
    p1 = cals[0]
    p2 = sum(cals)

    return (p1, p2)

