#!/usr/bin/env python3

import networkx as nx

def parser(line):
    aux = line.split(' ')
    return aux[1], aux[7]


def main():
    with open('input', 'r') as fp:
        data = [x for x in fp.read().split('\n')]
    depTree = nx.DiGraph()

    for line in data:
        node, child = parser(line)
        depTree.add_edge(node, child)

    part1 = nx.lexicographical_topological_sort(depTree)
    print(''.join(part1))


if __name__ == '__main__':
    main()
