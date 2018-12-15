#!/usr/bin/env python3

import collections
from pprint import pprint

def taxicab(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])




def main():
    with open('sinput', 'r') as fp:
        data = [map(int, x.split(', ')) for x in fp.readlines()]
    print(data)

    max_x = max(zip(*data)[0])
    max_y = max(zip(*data)[1])
    print(max_x. max_y)
        

if __name__ == '__main__':
    main()