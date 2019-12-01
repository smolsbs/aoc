#!/usr/bin/env python3

from math import floor

def main():
    with open('input', 'r') as fp:
        data = [int(x) for x in fp.readlines()]
    p1 = 0
    p2 = 0
    for i in data:
        p1 += fuel(i)
        b = fuel(i)
        while b > 0:
            p2 += b
            b = fuel(b)

    print("p1 = {}".format(p1))
    print("p2 = {}".format(p2))

def fuel(n):
    return floor(n/3) - 2


if __name__ == '__main__':
    main()