#!/usr/bin/env python3
import numpy as np

dirs = [(0,1), (1,0), (0, -1), (-1, 0), (1,1), (1,-1), (-1, 1), (-1,-1)]

def parse_seats(line):
    v = []
    for s in line:
        if s == 'L':
            v.append(0)
        else:
            v.append(-1)
    return v

def allpos(xx,yy):
    all_p = []
    for x in xx:
        for y in yy:
            all_p.append( (x,y) )
    return all_p

def part1(data):
    max_y = len(data)
    max_x = len(data[0])
    changed = 1
    new_d = np.copy(data)
    while changed:
        changed = 0
        for y in range(max_y):
            for x in range(max_x):
                if data[y,x] == -1:
                    continue
                near = data[max(0,y-1):y+2, max(0, x-1):x+2]
                n_occup = np.count_nonzero(near == 1) - data[y,x]
                if data[y, x] == 0:
                    if n_occup == 0:
                        new_d[ y, x] = 1
                        changed = 1
                elif data[y, x] == 1:
                    if n_occup >= 4:
                        new_d[y,x] = 0
                        changed = 1
        data = np.copy(new_d)
    
    all_occ = np.count_nonzero(data == 1)
    return all_occ

# SPAGHETT CODE
def part2(data):
    max_y = len(data)
    max_x = len(data[0])
    all_p = allpos(range(max_y), range(max_x))

    changed = 1
    new_d = np.copy(data)
    while changed:
        changed = 0
        for p in all_p:
            c_pos = p
            seats = 0
            for direct in dirs:
                new_p = (c_pos[0]+direct[0], c_pos[1]+direct[1])
                while (new_p[0] >= 0 and new_p[0] < max_y) and (new_p[1] >= 0 and new_p[1] < max_x):
                    if data[new_p[0], new_p[1]] == 1:
                        seats += 1
                        break
                    elif data[new_p[0], new_p[1]] == 0:
                        break
                    new_p = (new_p[0]+direct[0], new_p[1]+direct[1])
            if data[c_pos[0], c_pos[1]] == 0:
                if seats == 0:
                    new_d[c_pos[0], c_pos[1]] = 1
                    changed = 1
            elif data[c_pos[0], c_pos[1]] == 1:
                if seats >= 5:
                    new_d[c_pos[0], c_pos[1]] = 0
                    changed = 1
        data = np.copy(new_d)

    all_occ = np.count_nonzero(data == 1)
    return all_occ
      

def main():
    with open('input', 'r') as fp:
        data = np.array([parse_seats(x) for x in fp.read().split('\n')])
    
    p1 = part1(data)
    print("part 1: {}".format(p1))
    p2 = part2(data)
    print("part 2: {}".format(p2))

if __name__ == '__main__':
    main()