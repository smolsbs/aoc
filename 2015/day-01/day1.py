#!/usr/bin/env python3
#
from collections import Counter
def main():
    with open('input', 'r') as fp:
        data = fp.read()
    _sum = 0
    pos = 1
    for c in data:
        if c == '(': 
            _sum += 1
        elif c == ')':
            _sum -= 1
        if _sum == -1:
            print(pos)
        pos += 1
    print(_sum)


if __name__ == '__main__':
    main()