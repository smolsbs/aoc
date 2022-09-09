#!/usr/bin/python
from itertools import combinations

def main():
    total = 0
    lowest = 0
    with open('input', 'r') as fp:
        data = [int(x) for x in fp.read().strip().split('\n')]

    for i in range(2, 21):
        total_r = 0
        for c in combinations(data, i):
            if sum(c) == 150:
                total += 1
                total_r += 1
        if (lowest == 0 and total_r != 0 ):
            lowest = i
    print(f"Part 1: {total}\nPart 2: {lowest}")


if __name__ == '__main__':
    main()