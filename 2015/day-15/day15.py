#!/usr/bin/python

import sys

from re import match
from ortools.constraint_solver import pywrapcp


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

    solver.Add(solver.Sum(ingredients) == 100)
    caps_sum = solver.Sum(caps[i] * ingredients[i] for i in range(len(ingredients)))
    durs_sum = solver.Sum(durs[i] * ingredients[i] for i in range(len(ingredients)))
    flavs_sum = solver.Sum(flavs[i] * ingredients[i] for i in range(len(ingredients)))
    texts_sum = solver.Sum(texts[i] * ingredients[i] for i in range(len(ingredients)))
    
    solver.Add(caps_sum >= 0)
    solver.Add(durs_sum >= 0)
    solver.Add(flavs_sum >= 0)
    solver.Add(texts_sum >= 0)

    if part2 is not None:
        cals_sum = solver.Sum(cals[i] * ingredients[i] for i in range(len(ingredients)))
        solver.Add(cals_sum == part2)

    total = solver.IntVar(0, sys.maxsize, "Total")  # here
    solver.Add(total == caps_sum * durs_sum * flavs_sum * texts_sum)

    obj = solver.Maximize(total, 1)

    a = solver.Phase(ingredients + [total], solver.INT_VAR_DEFAULT, solver.INT_VALUE_DEFAULT)
    solver.NewSearch(a, [obj])
    best, best_ings = (None, None)
    while solver.NextSolution:
        best = total.Value()
        best_ings = [(i.Name(), i.Value()) for i in ingredients]

    print(best, best_ings)

    solver.EndSearch()

if __name__ == '__main__':
    main()
    main(500)