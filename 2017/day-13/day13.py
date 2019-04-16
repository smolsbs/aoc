#1 python

import collections
from re import findall

def runFirewall(wall, maxDepth):
    pos = 0
    pTime = 0
    severity = 0
    while pos < maxDepth:
        for d in wall:
            if wall[d][2]:
                wall[d][0] -= 1
                if wall[d][0] == 0:
                    wall[d][2] = False
            else:
                wall[d][0] += 1
                if wall[d][0] == wall[d][1]:
                    wall[d][2] = True

        pTime += 1
        pos += 1
        for d in wall:
            if wall[d][0] == 0:
                if pos == d:
                    severity += d * wall[d][1]
    return severity

def main():
    firewall = collections.defaultdict(list)
    with open('sinput') as fp:
        for line in fp.read().strip().split('\n'):
            layer, depth = map(int, findall(r'\d+', line))
            firewall[layer] = [0, depth, False]
    maxDepth = sorted(firewall.keys(), reverse=True)[0]
    print(runFirewall(firewall, maxDepth))

if __name__ == '__main__':
    main()