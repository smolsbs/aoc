#!/usr/bin/env python3
import re

def smallest(arr):
    m1 = min(arr)
    arr.pop(arr.index(m1))
    m2 = min(arr)
    return m1, m2

def main():
    paper = 0
    ribbon = 0
    with open('input', 'r') as fp:
        for line in fp.read().split('\n'):
            l, w, h = map(int, re.findall(r'-?\d+', line))
            m1, m2 = smallest([l, w, h])
            paper += 2*l*w + 2*w*h + 2*h*l + m1*m2
            ribbon += 2*m1 + 2*m2 + l*w*h
    print(paper)
    print(ribbon)

if __name__ == '__main__':
    main()