#!/usr/bin/env python3

def main():
    with open('input', 'r') as fp:
        data = [x for x in fp.read().split('\n')]
    nice = 0
    really_nice = 0
    for line in data:
        if vowels(line):
            if double(line):
                if blacklist(line):
                    nice += 1
        if pairs(line):
            if repeat(line):
                really_nice += 1
    print(nice)
    print(really_nice)


def pairs(_string):
    for i in range(len(_string)-3):
        sstring = _string[i:i+2]
        if sstring in _string[i+2:]:
            return True
    return False

def repeat(_string):
    for i in range(1, len(_string)-1):
        if _string[i-1] == _string[i+1]:
            return True
    return False

def vowels(_string):
    # count the number of different vowels present in the given string
    # if 3 or more, return true. Else return False
    c = 0
    for v in _string:
        if v in 'aeiou':
            c += 1
        if c >= 3:
            return True
    return False

def double(_string):
    # checks if there is two consecutive chars and returns True if so. Else returns False
    for i in range(len(_string)-1):
        if _string[i] == _string[i+1]:
            return True
    return False

def blacklist(_string):
    # check if patterns are in a given string. if so, return False. Else return True
    for sr in ['ab', 'cd', 'pq', 'xy']:
        if sr in _string:
            return False
    return True

if __name__ == '__main__':
    main()