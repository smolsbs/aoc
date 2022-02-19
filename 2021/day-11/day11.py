#!/usr/bin/env python3

import numpy as np
import aocUtils

MAX = 10

def neighbour_coords(y, x):
    """Creates a list for the neighbour elements to coord (y,x)

    Args:
        y (int): y coord
        x (int): x coord

    Returns:
        list: list of neighboring elements
    """
    aaa = []
    for _y in range(max(y-1, 0), min(y+2, MAX)):
        for _x in range(max(x-1, 0), min(x+2, MAX)):
            aaa.append((_y, _x))
    aaa.remove((y, x))
    return aaa


def iterate(grid) -> (int, int):
    n_flashes = 0       # part 1
    all_flashed = None  # part 2

    i = 0
    # iterate the grid until the part 2 sol is found
    while all_flashed is None:
        i += 1      # iteration tracker
        grid += 1   # adds 1 to every element

        flashed_elems = set()   # tracks elements that have flashed
        flashed = True

        while flashed:
            # check if there are elems that are greater than 9
            # break this while loop if not
            res = np.where(grid > 9)
            if len(res[0]) == 0:
                flashed = False
                continue

            # get all the positions that are greater than 9
            flashes = list(zip(res[0], res[1]))

            for a, b in flashes:
                grid[a,b] = 0

                # the counter for part 1, stop adding after iteration 100
                if i <= 100:
                    n_flashes += 1

                flashed_elems.add((a,b))

                # get the neighboring elements
                neighs = neighbour_coords(a, b)

                # add 1 to the neighbours only if they're
                # not in the flashed_elems set
                # since we cannot add to a previously flashed element
                for c, d in neighs:
                    if (c,d) not in flashed_elems:
                        grid[c,d] += 1
        
        if len(flashed_elems) == 100:
            all_flashed = i

    return n_flashes, all_flashed



def main():
    data = aocUtils.loadInput('input')

    grid = np.array([[int(x) for x in line] for line in data])

    p1, p2 = iterate(grid)

    print(f'part1: {p1}')
    print(f'part2: {p2}')

if __name__ == '__main__':
    main()
