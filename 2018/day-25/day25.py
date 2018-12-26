#!/usr/bin/env python3
#
import networkx

def manhattan(p1, p2):
    return sum(abs(a-b) for a, b in zip(p1, p2))


def main():
    points = set()
    # with open('sinput', 'r') as fp:
    with open('input', 'r') as fp:
        for line in fp.read().split('\n'):
            points.add(tuple(map(int, line.split(","))))

    N = networkx.Graph()
    for p1 in points:
        for p2 in points:
            if manhattan(p1, p2) <= 3:
                N.add_edge(p1, p2)
    print(networkx.number_connected_components(N))
    
if __name__ == '__main__':
    main()