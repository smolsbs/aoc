#!/usr/bin/env python3

from collections import Counter
from re import match, findall

def bool2int(b):
    if b:
        return 1
    return 0

def main():
    pattern = r'(\d+)-(\d+) (\w): (\w+)'
    with open('input', 'r') as fp:
        data = [x for x in fp.readlines()]

    part_1 = 0
    part_2 = 0

    for line in data:
        (l, u, c, pw) = findall(pattern, line)[0]
        aux = Counter(pw)
        if aux[c] >= int(l) and aux[c] <= int(u):
            part_1 +=1
            
        # using XOR to get either one or another
        if bool2int(c == pw[int(l)-1] ) ^ bool2int(c == pw[int(u)-1]):
            part_2 +=1

    print('part 1: {}'.format(part_1))
    print('part 2: {}'.format(part_2))

if __name__ == '__main__':
    main()