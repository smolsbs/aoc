#!/usr/bin/python
from itertools import combinations

def main():
    total = 0
    with open('input', 'r') as fp:
        data = [int(x) for x in fp.read().strip().split('\n')]

    for i in range(2, 21):
        total_r = 0
        for c in combinations(data, i):
            if sum(c) == 150:
                total += 1
                total_r += 1
        print("20 C {:2}: {}".format(i, total_r))

    print(total)


if __name__ == '__main__':
    main()