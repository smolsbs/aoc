#!/usr/bin/env python3

import AoCUtils
from pprint import pprint
from anytree import Node

def main():
    # data = AoCUtils.loadInput('input')
    data = AoCUtils.loadInput('sinput')

    orbits = Node("COM")
    for line in data:
        print(line)
        

if __name__ == '__main__':
    main()