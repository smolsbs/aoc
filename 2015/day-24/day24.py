#!/usr/bin/python


from itertools import combinations
from operator import mul
from functools import reduce


def getQe(lyst, nParts):
    # the sum of any given group of weigths so that every group weights the same
    groupWeight = sum(lyst) // nParts    
    
    qE = []
    for i in range(4, 8):
        for w in list(combinations(lyst, i)):
            if sum(w) == groupWeight:
                qE.append((w, reduce(lambda x,y : x*y, w)))

    return qE[0]


def main():
    with open('input', 'r') as fp:
        packages = [int(x) for x in fp.read().strip().split('\n')]
    
    print(getQe(packages, 3))   # part 1
    print(getQe(packages, 4))   # part 2
    

if __name__ == '__main__':
    main()