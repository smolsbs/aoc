#!/usr/bin/env python3

import AoCUtils
from pprint import pprint
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def addChildren(self, child):
        self.children.append(child)

def makeTree(nodes, start):
    tree = {start: {}}
    for child in nodes[start]:
        print(start, child)
        if child in nodes.keys():
            tree[start][child] = makeTree(nodes, child)
        else:
            return child
        print(tree)
    return tree


def main():
    # data = AoCUtils.loadInput('input')
    data = AoCUtils.loadInput('sinput')

    planetNodes = {}

    # make all the necessary nodes for then creating the tree
    for line in data:
        (parent, child) = line.split(')')

        if parent not in planetNodes.keys():
            planetNodes[parent] = [child]
        else:
            planetNodes[parent].append(child)

    # pprint(planetNodes)        
    b = makeTree(planetNodes, 'COM')

    pprint(b)
    
if __name__ == '__main__':
    main()