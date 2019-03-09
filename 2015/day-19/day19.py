#!/usr/bin/python
import re
from collections import Counter, defaultdict


def parseKeys(data):
    keys = defaultdict(list)
    for line in data:
        key, pat = line.split(' => ')
        keys[key].append(pat)
    return keys


def produceMolecules(strand, pat, repl):
    newMolecules = []
    for r in repl:
        for i in range(1, len(strand)):
            newMolecules.append(pat.join(strand[0:i]) + r + pat.join(strand[i:]))

    return newMolecules


def main():
    molecules = Counter()
    with open('input', 'r') as fp:
        data = [x.strip('\n') for x in fp.readlines()]
        keys = parseKeys(data[:-2])
        strand = data[-1]

    for pat, replList in keys.items():
        brokenStrand = strand.split(pat)
        molecules.update(produceMolecules(brokenStrand, pat, replList))
    print(sum(1 for c in molecules.values()))

if __name__ == '__main__':
    main()