#!/usr/bin/env python3

import aocUtils

def part1(data):
    _increases = 0
    # set first value to curr_val
    curr_val = data[0]

    # iterate over the remaining values in data, check if they are greater than
    # curr_val, and set v as curr_val for the next loop
    for v in data[1:]:
        if v > curr_val:
            _increases += 1
        curr_val = v

    return f'part 1: {_increases}'


def part2(data):
    _increases = 0

    # set the sum of the first three vals as curr_val
    curr_val = sum(data[:3])

    # loop thought the list from index 1 to index len()-2
    for i in range(1, len(data)-2):
        val = sum(data[i:i+3])
        if val > curr_val:
            _increases += 1
        curr_val = val

    return f'part 2: {_increases}'

def main():

    data = aocUtils.loadInput('input', int)
    # with open('input', 'r') as fp:
        # data = [int(x) for x in fp.read().strip().split('\n')]

    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()
