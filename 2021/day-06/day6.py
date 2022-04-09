#!/usr/bin/env python3

import aocUtils

PART1 = 80
PART2 = 256

def parse_input(_input):
    _ret = [0 for _ in range(9)]
    for f in map(int, _input.strip().split(',')):
        _ret[f] += 1

    return _ret

# thanks r/adventofcode for the hints
def simulate(data, max_days):
    fishes = parse_input(data[0])

    for _ in range(max_days):
        heaven = fishes[0]
        for i in range(1,9):
            fishes[i-1] = fishes[i]
        fishes[6] += heaven
        fishes[8] = heaven

    return sum(fishes)

def main():
    data = aocUtils.loadInput('input')

    p1 = simulate(data, PART1)
    p2 = simulate(data, PART2)

    print(f'part 1: {p1}')
    print(f'part 2: {p2}')

if __name__ == '__main__':
    main()