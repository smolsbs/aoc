#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations

def best(people, relations):
    best = (0, [])
    for s in permutations(people, len(people)):
        _sum = 0
        for i in range(len(people)):
            _sum += relations[s[i]][s[(i-1) % len(people)]] + relations[s[i]][s[(i+1) % len(people)]]
        if _sum > best[0]:
            best = (_sum, s)
    
    return best

def main():
    happy = defaultdict(lambda: {})
    with open('input', 'r') as fp:
        for line in fp.read().strip().split('\n'):
            a = line.split(' ')
            if a[2] == "gain":
                happy[a[0]][a[-1][:-1]] = int(a[3])
            else:
               happy[a[0]][a[-1][:-1]] = -int(a[3])
    people = list(happy.keys())
    
    print(best(people, happy)[0])  # part 1

    for p in people:
        happy[p]["Me"] = 0
        happy["Me"][p] = 0
    people.append("Me")
    print(best(people, happy)[0])  # part 2



if __name__ == '__main__':
    main()