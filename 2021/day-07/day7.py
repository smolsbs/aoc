#!/usr/bin/env python3

import aocUtils
import numpy as np

def part1(data):
    goal_pos = np.int(np.median(data))
    fuel = 0
    for point in data:
        fuel += np.abs(goal_pos - point)

    return np.int(fuel)

def part2(data):
    mean = np.mean(data)
    checks = [np.floor(mean), np.ceil(mean)] # correct pos should be in here
    costs = {}

    for goal in checks:
        fuel = 0
        for point in data:
            dist = int(np.abs(goal - point))
            fuel += np.sum(list(range(1, dist+1)))
        costs[goal] = fuel

    k = sorted(costs, key=costs.get)[0]
    
    return np.int(costs[k])

def main():
    data = list(map(int, aocUtils.getInts('input')[0]))

    p1 = part1(data)
    p2 = part2(data)

    print(f'part1: {p1}')
    print(f'part2: {p2}')


if __name__ == '__main__':
    main()