#!/usr/bin/env python3
from collections import Counter, defaultdict

def main():
    with open('input', 'r') as fp:
        data = fp.read()

    houses = defaultdict(lambda: 0)

    sx = sy = rx = ry = 0
    houses[(0, 0)] += 2
    odd = True
    for step in data:
        if odd:
            if step is '>':
                sx += 1
            elif step is '<':
                sx -= 1
            elif step is '^':
                sy += 1
            elif step is 'v':
                sy -= 1
            coords = (sx, sy)
        else:
            if step is '>':
                rx += 1
            elif step is '<':
                rx -= 1
            elif step is '^':
                ry += 1
            elif step is 'v':
                ry -= 1
            coords = (rx, ry)
        
        houses[coords] += 1
        odd = not odd

    print(len(houses.keys()))

if __name__ == '__main__':
    main()