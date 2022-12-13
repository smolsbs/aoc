#!/usr/bin/env python3

from re import findall
from operator import add, mul
from copy import deepcopy
from numpy import prod

class Monkey:
    def __init__(self, monkey_id, items, op, div, on_true, on_false):
        self.id = monkey_id
        self.items = items
        self.second_term = self.parse_operation(op)
        self.divisible = div
        self.on_true = on_true
        self.on_false = on_false
        self.checked = 0

    def parse_operation(self, op):
        aux = op.split(' = ')[1].split(' ')

        if aux[2] == 'old':
            b = 'old'
        else:
            b = int(aux[2])

        if aux[1] == '+':
            self.run = lambda x,y: add(x,y)
        elif aux[1] == '*':
            self.run = lambda x,y: mul(x,y)

        self.operator = aux[1]
        return b


def check_items(monkey, list_of_monkeys, p2=None):
    while True:
        try:
            item = monkey.items.pop(0)
        except IndexError:
            break
        if monkey.second_term == 'old':
            b = item
        else:
            b = monkey.second_term

        new_worry = monkey.run(item, b)

        if not p2:
            new_worry //= 3
        else:
            new_worry = (new_worry % p2)

        if (new_worry % monkey.divisible) == 0:
            list_of_monkeys[monkey.on_true].items.append(new_worry)
        else:
            list_of_monkeys[monkey.on_false].items.append(new_worry)
        monkey.checked += 1

def solve_part_1(list_of_monkeys):

    for _round in range(20):
        for monkey in list_of_monkeys.values():
            check_items(monkey, list_of_monkeys)

    p1 = sorted([v.checked for v in list_of_monkeys.values()], reverse=True)[:2]

    return p1[0]*p1[1]

def solve_part_2(list_of_monkeys):
    # hi r/adventofcode
    beegmodule = prod([v.divisible for v in list_of_monkeys.values()])

    for _round in range(10000):
        for monkey in list_of_monkeys.values():
            if len(monkey.items) != 0:
                check_items(monkey, list_of_monkeys, beegmodule)

    p2 = sorted([v.checked for v in list_of_monkeys.values()], reverse=True)[:2]

    return p2[0]*p2[1]


def loadInput(path):
    with open(path, 'r', encoding='utf-8') as fp:
        lines = fp.read().strip().split('\n')

    monkeys = {}
    for idx in range(0, len(lines), 7):
        monkey_id = int(findall(r"\d+", lines[idx])[0])
        items = list(map(int, findall(r"\d+", lines[idx+1])))
        op = lines[idx+2].split(':')[1].strip()
        test = int(findall(r"\d+", lines[idx+3])[0])
        on_true = int(findall(r"\d+", lines[idx+4])[0])
        on_false = int(findall(r"\d+", lines[idx+5])[0])
        monkeys[monkey_id] = Monkey(monkey_id, items, op, test, on_true, on_false)

    return monkeys

def run(path):
 
    list_of_monkeys = loadInput(f"{path}/input")
    p1 = solve_part_1(deepcopy(list_of_monkeys))
    p2 = solve_part_2(deepcopy(list_of_monkeys))
    return p1, p2

