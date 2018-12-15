#!/usr/bin/env python3
# NOTE: inspitarion from this video https://www.youtube.com/watch?v=YQjPXSlSelc
# First part I was able to do by myself, but couldn't manage to make the second part work
# see old-day4.py

from collections import defaultdict

def main():
    with open('input', 'r') as fp:
        data = sorted([x.strip('\n') for x in fp.readlines()])

    Guard_minutes = defaultdict(lambda: (0, [0 for x in range(60)]))


    currID = None
    zzz = None
    for line in data:
        item = line.split(' ')
        time = int(item[1][3:5])
        if "Guard" in line:
            currID = item[3][1:]
            time_sleep = None
        if "asleep" in line:
            time_sleep = time
        if "wakes" in line:
            for i in range(time_sleep, time):
                Guard_minutes[currID] += 1
    print(Guard_minutes)



main()  