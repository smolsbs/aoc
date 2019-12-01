#!/usr/bin/env python3

def fuel(n):
    return n // 3 - 2       # huh, guess n // 3 does the flood division, neat

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

    print("p1 = {}\np2 = {}".format(p1, p2))


if __name__ == '__main__':
    main()