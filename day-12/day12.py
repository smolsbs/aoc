#!/usr/bin/env python3
# pylint: disable=C0103, C0111

from collections import defaultdict
# from pprint import pprint

def parse(c):
    if c == '#':
        return '1'
    return '0'

def main():
    # ...## => #
    # ..#.. => #
    rules = defaultdict(list)
    with open('sinput', 'r') as fp:
        data = fp.read().split('\n')
        init_state = [0,0,0] + [parse(c) for c in data[0].split(' ')[2]] + [0,0,0,0,0,0]
        for rule in data[2:]:
            out = parse(rule[-1])
            rules[out].append([parse(c) for c in rule[:5]])

    gen = 0
    state = init_state
    state_len = len(init_state)
    while gen < 21:
        for i in range(state_len):
            if i == 0:
                pot = state[-2:] + state[:3]
            elif i == 1:
                pot = state[:-1] + state[:4]
            elif i == state_len - 2:
                pot = state[-4:] + state[0:]
            elif i == state_len - 1:
                pot = state[-3:] + state[:1]
            else:
                pot = state[i-2:i+3]
            if pot in rules['1']:
                state[i] = '1'
            elif pot in rules['0'] or pot not in rules.values():
                state[i] = '0'
        print(''.join(state).replace('1','#').replace('0','.'))
        gen += 1
    s=0
    print()
    for i in range(len(state)):
        if state[i] == 1:
            s += i
    print(s)
if __name__ == '__main__':
    main()
