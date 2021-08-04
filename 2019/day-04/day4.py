#!/usr/bin/env python3

from collections import Counter

import AoCUtils


# part 1
def checkPass(pw):
    pw = str(pw)
    double = False
    for i in range(len(pw)-1):
        if int(pw[i]) > int(pw[i+1]):
            return False
        if int(pw[i]) == int(pw[i+1]):
            double = True

    if double:
        return True
    return False

# part 2
def secondCheck(pw):
    a = Counter(str(pw)).most_common()
    mc = a[0][1]
    rest = [x[1] for x in a[1:]]

    if mc > 2:
        if 2 in rest:
            return True
    elif mc == 2:
        return True
    return False


def main():
    data = AoCUtils.loadInput('input')[0]
    rang = tuple(map(int, data.split('-')))
    (p1, p2) = 0,0
    for pw in range(rang[0], rang[1]+1):
        if checkPass(pw):
            p1 += 1
            if secondCheck(pw):
                p2 += 1
    print("part1: {}\npart2: {}".format(p1, p2))

if __name__ == '__main__':
    main()
