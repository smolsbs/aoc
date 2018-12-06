#!/usr/bin/env python3
from collections import defaultdict

def main():
    with open('input', 'r') as fp:
        data = sorted([x.strip('\n') for x in fp.readlines()])

    shifts = defaultdict(lambda: [])

    currID = None
    for line in data:
        item = line.split(' ')
        if "Guard" in line:
            currID = int(item[3][1:])
            status = None
            continue
            t = None
        if "asleep" in line:
            t = int(item[1][3:5])
            status = 'z'
        if "wakes" in line:
            t = int(item[1][3:5])
            status = 'w'

        shifts[currID].append([status, t])

    worst = (0, 0, 0)   # id, total sleep, minute
    for key, val in shifts.items():
        s = 0
        mins = [0 for x in range(60)]
        for i in range(0, len(val), 2):
            s += (val[i+1][1] - val[i][1])
            for j in range(val[i][1], val[i+1][1]):
                mins[j] += 1

        if s > worst[1]:
            worst = (key, s, mins.index(max(mins)))
    print(worst[0]*worst[2])
main()  