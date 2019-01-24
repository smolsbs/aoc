#!/usr/bin/python

from collections import defaultdict

MESSAGE = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
            "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

def main():
    sues = defaultdict(lambda: {})

    with open('input', 'r') as fp:
        for line in fp.read().replace(":", "").replace(",", "").split('\n'):
            i = line.split(" ")[1]
            line = line.split(" ")[2:]
            for j in range(int(len(line)/2)):
                sues[i][line[2*j]] = int(line[2*j+1])

    for i, gifts in sues.items():
        # part 1 checks
        possible = True
        for gift, amount in gifts.items():
            if amount != MESSAGE[gift]: 
                possible = False
                break
        if possible:
            print("part1: %s" % i)

        # part 2 checks
        possible = True
        for gift, amount in gifts.items():
            if gift in ["cats", "trees"]:
                if amount <= MESSAGE[gift]:
                    possible = False
                    break
            elif gift in ["pomeranians", "goldfish"]:
                if amount >= MESSAGE[gift]:
                    possible = False
                    break
            else:
                if amount != MESSAGE[gift]: 
                    possible = False
                    break
        if possible:
            print("part2: %s" % i)

if __name__ == '__main__':
    main()