#!/usr/bin/python

from collections import defaultdict

def parse(value):
    if value.startswith('R'):
        return (int(value[1:]), 1)
    return (int(value[1:]), 0)

def main():
    with open('input', 'r') as fp:
        data = [parse(x) for x in fp.read().strip().split(', ')]
    
    x, y = (0, 0)
    compass = 0     # 0 for N, 1 for E, 2 for S, 3 for W
    pos = set()
    p2Found = False
    for inst in data:
        if inst[1] == 1:
            compass = (compass + 1) % 4
        else:
            compass = (compass - 1) % 4
        for n in range(inst[0]):
            if compass == 0 or compass == 2:
                if compass == 0:
                    x += 1
                else:
                    x -= 1
            elif compass == 1 or compass == 3:
                if compass == 1:
                    y += 1
                else:
                    y -= 1
            if (x, y) in pos and not p2Found:
                print("p2: {}".format(abs(x)+abs(y)))
                p2Found = True
            else:
                pos.add((x, y))

    print("p1: {}".format(abs(x)+abs(y)))


if __name__ == '__main__':
    main()