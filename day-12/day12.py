#!/usr/bin/env python3
# pylint: disable=C0103, C0111

from collections import defaultdict

def main():
    with open('input', 'r') as fp:
        data = fp.read().split('\n')
        state = '....' + data[0].split(' ')[2] + ''.join('.' for _ in range(2000))
        rules = defaultdict(list)
        for rule in data[2:]:
            out = rule[-1]
            rules[out].append(rule.split(' ')[0])
    _sum, amount, i = iterator(state, rules)

    print("Part 2: %d" % (_sum + amount * (50000000000 - i)))


def iterator(flowerpots, rules):
    gen = 0
    _len = len(flowerpots)
    diff = 0
    prev_s = 0
    while True:
        new_state = ''
        for i in range(_len):
            if i == 0:
                pot = flowerpots[-2:] + flowerpots[:3]
            elif i == 1:
                pot = flowerpots[:-1] + flowerpots[:4]
            elif i == _len - 2:
                pot = flowerpots[-4:] + flowerpots[0:]
            elif i == _len - 1:
                pot = flowerpots[-3:] + flowerpots[:1]
            else:
                pot = flowerpots[i-2:i+3]
            if pot in rules['#']:
                new_state += '#'
            elif pot in rules['.'] or pot not in rules.values():
                new_state += '.'
        flowerpots = new_state
        gen += 1
        s = 0
        for i in range(_len):
            if flowerpots[i] == '#':
                s += (i-4)
        if gen == 20:
            print("Part 1: %d" % s)
        if (s - prev_s) == diff:
            return (prev_s, diff, gen-1)
        diff = s - prev_s
        prev_s = s


if __name__ == '__main__':
    main()
