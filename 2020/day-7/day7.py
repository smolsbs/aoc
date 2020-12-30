#!/usr/bin/env python3

from collections import defaultdict

def main():
    with open('example', 'r') as fp:
        data = [x for x in fp.readlines()]

    for line in data:
        a = line.strip().split(' contain ')
        print(a)

if __name__ == '__main__':
    main()