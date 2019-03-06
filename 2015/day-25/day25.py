#!/usr/bin/python

from re import findall

def nextNumber(n):
    return (n*252533) % 33554393


def main():
    with open('input', 'r') as fp:
        inp = tuple(map(int, findall(r'(\d+)', fp.read())))
    
    n = 20151125
    x, y = (1, 1)

    while True:
        if y == 1:
            y = x +1
            x = 1
            print("row: %d" % y)
        else:
            y -= 1
            x += 1
        n = nextNumber(n)
        if (y, x) == inp:
            print(n)
            break

if __name__ == '__main__':
    main()