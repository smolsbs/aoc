#!/usr/bin/env python3
import numpy as np
import multiprocessing

with open('input', 'r') as fp:
    GRID_ID = int(fp.read().strip('\n'))

def main():
    fuel_grid = fuel_power(300)
    print("%d,%d" % find_best_power(fuel_grid))
    find_best_power_size(fuel_grid, 3, 20)
    

def fuel_power(size):
    global GRID_ID
    grid = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(300):
        for j in range(300):
            rack_id = (j + 1) + 10
            p_level = rack_id * (i + 1) + GRID_ID
            p_level *= rack_id
            grid[j][i] = (p_level // 100 % 10) - 5
    return grid

def find_best_power(grid):
    best = 0
    coord = None
    for i in range(298):
        for j in range(298):
            s = sum(grid[i][j:j+3]) + sum(grid[i+1][j:j+3]) + sum(grid[i+2][j:j+3])
            if s > best:
                best = s
                coord = (i+1, j+1)
    return coord

def find_best_power_size(grid, init, end):
    # yay O(n^5)
    for size in range(init, end):
        best = 0
        x, y = 0, 0
        for i in range(0, 300-size):
            for j in range(0, 300-size):
                s = 0
                for t in range(size + 1):
                    s += sum(grid[j+t][i:i+size+1])
                if s > best:
                    best = s
                    x, y =  j+1, i+1

        print("{},{},{} max={}".format(x, y, size, best))

if __name__ == '__main__':
    main()