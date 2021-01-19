#!/usr/bin/env python3

from itertools import combinations

def main():
    with open('input', 'r') as fp:
        data = [int(x.strip()) for x in fp.read().split('\n')]

    # part 1
    for p in range(25, len(data)):
        all_sums = set( sum(x) for x in combinations(data[p-25:p], 2))
        if data[p] not in all_sums:
            p1 = data[p]
            print("part 1: %d" % data[p])
            break
    
    # part 2
    for leng in range(2, len(data)-1):
        for pos in range(0, len(data)-leng):
            cont_set = data[pos:pos+leng]
            smal = min(cont_set)
            larg = max(cont_set)
            if sum(cont_set) == p1:
                print("part 2: %d" % (smal+larg))
                return

if __name__ == '__main__':
    main()