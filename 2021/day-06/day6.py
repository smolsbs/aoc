#!/usr/bin/env python3

import aocUtils

PART1 = 80
PART2 = 256

def parse_fishes(_input):
    fishes = list(map(int, _input.strip().split(',')))
    _ret = {k:0 for k in list(range(9))}
    for f in fishes:
        _ret[f] += 1

    return _ret

# thanks r/adventofcode for the hints
def new_algo(data, max_days):
    fishes = parse_fishes(data[0])

    # instead of tracking every single fish because this will blow up really fast
    # for the later days, track the range of days 
    # left alive where each day has the number of current fishes
    # For each new day, copy the number of fishes from day i to day i-1
    # if i=0, add number of fishes to i=6 and set i=8, amount of new fishes, to fishes[0]
    for _ in range(max_days):
        new_fishes = {k:0 for k in list(range(9))}
        for i in range(1,9):
            new_fishes[i-1] = fishes[i]
        new_fishes[6] += fishes[0]
        new_fishes[8] = fishes[0]
        fishes = new_fishes

    return sum(fishes.values())

def main():
    data = aocUtils.loadInput('input')

    p1 = new_algo(data, PART1)
    p2 = new_algo(data, PART2)

    print(f'part 1: {p1}')
    print(f'part 2: {p2}')

# works for part 1, impossible to run on part 2 since the list becomes
# so big it will eat the entire memory from the system
# def old_algo(fishes):
#     fishes = fishes[:]
#     for _ in range(PART1):
#         print(f'day {_+1}')
#         for i in range(len(fishes)):
#             fishes[i] -= 1
#             if fishes[i] < 0:
#                 fishes[i] = 6
#                 fishes.append(8)
#         # pprint(fishes)
#     print(len(fishes))

if __name__ == '__main__':
    main()