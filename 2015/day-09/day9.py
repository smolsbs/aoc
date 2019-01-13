#!/usr/bin/env python3
from collections import defaultdict
def main():
    places = defaultdict(lambda: {})
    visited = []
    with open('input', 'r') as fp:
        for line in fp.read().split('\n'):
            a = line.split(' ')
            places[a[0]][a[2]] = int(a[4])
            places[a[2]][a[0]] = int(a[4])
            if a[0] not in visited:
                visited.append(a[0])
            if a[2] not in visited:
                visited.append(a[2])
    shortest = None

    for k1, d in places:
        for k2, v in d:
            

    print(places)

if __name__ == '__main__':
    main()