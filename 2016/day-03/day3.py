#!/usr/bin/python

from re import findall
from collections import defaultdict
from itertools import combinations

def sortSides(triangles):
    for i in range(len(triangles)):
        triangles[i] = sorted(triangles[i])

def part1(numbers):
    sortSides(numbers)
    isTriangle = 0
    for t in numbers:
        if t[0] + t[1] > t[2]:
            isTriangle += 1

    print(isTriangle)

def part2(numbers):
    isTriangle = 0
    for i in range(3):
        for n in range(0, len(numbers)//3, 3):
            t1, t2, t3 = sorted([numbers[n][i], numbers[n+1][i], numbers[n+2][i]])
            if t1+t2 > t3:
                isTriangle += 1
    print(isTriangle)


def main():
    with open('input', 'r') as fp:
        triangles = []

        for line in fp.read().strip().split('\n'):
            triangles.append(list(map(int, findall(r'(\d+)', line))))
    t2 = triangles
    part1(triangles)
    part2(t2)


if __name__ == '__main__':
    main()
