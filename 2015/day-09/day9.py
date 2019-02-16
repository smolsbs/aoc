#!/usr/bin/env python3
from collections import defaultdict
from itertools import permutations


def main():
    places = defaultdict(lambda: {})
    with open('input', 'r') as fp:
        for line in fp.read().split('\n'):
            a = line.split(' ')
            places[a[0]][a[2]] = int(a[4])
            places[a[2]][a[0]] = int(a[4])
    shortest = None
    longest = None
    ways = list(permutations(places.keys(), 8))
    for trip in ways:
        _sum = sum([places[trip[i]][trip[i+1]] for i in range(7)])
        if shortest is None:
            shortest = _sum
        if _sum < shortest:
            shortest = _sum
        if longest is None:
            longest = _sum
        if _sum > longest:
            longest = _sum

    print(shortest)
    print(longest)
if __name__ == '__main__':
    main()