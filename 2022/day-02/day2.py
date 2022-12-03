#!/usr/bin/env python3


RULES = {'A': {'X':0, 'Y': 1, 'Z':-1},
         'B': {'X':-1, 'Y': 0, 'Z':1},
         'C': {'X':1, 'Y': -1, 'Z':0}}

RULES_V2 = {'A': {'X': 'C', 'Y':'A', 'Z': 'B'},
            'B': {'X': 'A', 'Y':'B', 'Z': 'C'},
            'C': {'X': 'B', 'Y':'C', 'Z': 'A'}}

def solve(data):
    score = 0
    score_v2 = 0
    for play in data:
        opp, me = play
        score += ord(me) - 87 + (3 + 3*(RULES[opp][me]))
        score_v2 += 3*(ord(me)-88) + ord(RULES_V2[opp][me]) - 64
    return score, score_v2

def load_data(path):
    plays = []
    with open(path, 'r') as fp:
        for line in fp.read().strip().split('\n'):
            a,b = line.split(' ')
            plays.append((a,b))

    return plays

def run(path):

    data = load_data(f"{path}/input")

    p1, p2 = solve(data)

    return (p1, p2)
