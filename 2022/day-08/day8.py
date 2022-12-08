#!/usr/bin/env python3

from itertools import combinations_with_replacement
import numpy as np


def check_row(arr, r, c):
    row_max = arr.shape[0]

    t_u = 0
    t_d = 0

    # going up
    v_u = True
    for p in range(r-1, -1, -1):
        if arr[p, c] >= arr[r, c]:
            v_u = False
            t_u += 1
            break
        t_u += 1

    #going down
    v_d = True
    for p in range(r+1, row_max):
        if arr[p,c] >= arr[r,c]:
            v_d = False
            t_d += 1
            break
        t_d += 1

    return (v_u or v_d), (t_u * t_d)

def check_col(arr, r, c):
    col_max = arr.shape[1]

    t_l = 0
    t_r = 0

    # going left
    v_l = True
    for p in range(c-1, -1, -1):
        if arr[r,p] >= arr[r,c]:
            v_l = False
            t_l += 1
            break
        t_l += 1

    #going right
    v_r = True
    for p in range(c+1, col_max):
        if arr[r,p] >= arr[r,c]:
            v_r = False
            t_r += 1
            break
        t_r += 1

    return (v_l or v_r), (t_l * t_r)

def solve(arr):
    arr_len = arr.shape[0]

    visible_trees = 4*(arr_len-1) # all the outer edge trees are visible already
    scenic_score = 0

    pos = combinations_with_replacement(range(1,arr_len-1), 2)

    for i,j in pos:
        v_ud, t1 = check_row(arr, i, j)
        v_lr, t2 = check_col(arr, i, j)
        visible_trees += 1 if (v_ud or v_lr) else 0

        if t1*t2 > scenic_score:
            scenic_score = t1*t2

    return visible_trees, scenic_score

def loadArray(path):

    with open(path, 'r', encoding='utf-8') as fp:
        data = fp.read().strip().split('\n')
        _len = len(data[0])

    arr = np.zeros((_len, _len), dtype=int)

    for l, idx in zip(data, range(_len)):
        arr[idx,:] = list(map(int, list(l)))

    return arr

def run(path):
    arr = loadArray(f"{path}/input")

    return solve(arr)
