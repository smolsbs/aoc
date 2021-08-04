#!/usr/bin/env python3

import AoCUtils

def fuel(n):
    return n // 3 - 2       # huh, guess n // 3 does the floor division, neat

def main():
    data = AoCUtils.loadInput('input', int)
    p1 = 0
    p2 = 0
    for i in data:
        p1 += fuel(i)
        b = fuel(i)
        while b > 0:
            p2 += b
            b = fuel(b)

    print("p1 = {}\np2 = {}".format(p1, p2))


if __name__ == '__main__':
    main()