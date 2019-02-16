#!/usr/bin/python

import sys

from re import match


def main(part2=None):
    ingredients, caps, durs, flavs, texts, cals = [], [], [], [], [], []
    solver = pywrapcp.Solver("Max")
    regex = r'(\w+): capacity (\-?\d+), durability (\-?\d+), flavor (\-?\d+), texture (\-?\d+), calories (\-?\d+)'
    with open('input', 'r') as fp:
        for line in fp.read().strip().split('\n'):
            ing, cap, dur, flav, text, cal = match(regex, line).groups()
            _ingredient = solver.IntVar(0, 99, ing)
            solver.Add(_ingredient >= 0)
            ingredients.append(_ingredient)
            caps.append(int(cap))
            durs.append(int(dur))
            flavs.append(int(flav))
            texts.append(int(text))
            cals.append(int(cal))


if __name__ == '__main__':
    main()
    # main(500)
