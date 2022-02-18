#!/usr/bin/env python3

from collections import *
from queue import Queue
import aocUtils
import numpy as np


def algo(grid: np.ndarray, start:tuple, end:tuple):
    frontier = Queue()
    frontier.put(start)
    reached = set()
    reached.add(start)
    pass





def main():
    data = aocUtils.loadInput('sinput')
    asdf = np.array([[x for x in line] for line in data])

    print(type(asdf))
    # row, column
    start = (0,0)
    end = (len(asdf)-1, len(asdf[0,])-1)
    
    print(start, end)

    p1 = None
    p2 = None

    # print(f'part1: {p1}')
    # print(f'part2: {p2}')

if __name__ == '__main__':
    main()
