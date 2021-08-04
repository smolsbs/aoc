#!/usr/bin/env python3

from re import findall
from collections import defaultdict
import AoCUtils

def main():
    # data = AoCUtils.loadInput('input')
    data = AoCUtils.loadInput('sinput')
    simpleReacts = defaultdict(list)
    compReacts = defaultdict(list)
    for line in data:
        a = line.split(' => ')

        if ',' in a[0]:
            c = a[0].split(', ')
            print(c)
        else:
            (sQuant, sComp) = a[0].split(' ')
            (fQuant, fComp) = a[1].split(' ')
            
            



if __name__ == '__main__':
    main()