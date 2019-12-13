#!/usr/bin/env python3

from itertools import combinations
from hashlib import md5
from numpy import lcm
from collections import defaultdict
from AoCUtils import getInts


COORDS = {'x', 'y', 'z'}

def sumVelToPos(planets):
    for p in planets:
        for v in COORDS:
            p['pos'][v] += p['vel'][v]

def hashPlanets(planets, cord):
    a = []
    for p in planets:
        a.append(str(p['pos'][cord]))
        a.append(str(p['vel'][cord]))
    h = ' '.join(a)
    hashed = md5(h.encode()).hexdigest()
    return bytes(hashed, 'utf-8')

def getEnergy(planet):
    pot = sum([ abs(v) for k,v in planet['pos'].items()])
    kin = sum([ abs(v) for k,v in planet['vel'].items()])
    return pot*kin

def simulation(planets, pairs, steps, p2=False):
    if p2:
        found = set()
        hashes = defaultdict(set)
        cords = {'x':None, 'y':None, 'z':None}
    for s in range(steps):
        for p in pairs:
            for c in COORDS:
                if planets[p[0]]['pos'][c] > planets[p[1]]['pos'][c]:
                    planets[p[0]]['vel'][c] -= 1
                    planets[p[1]]['vel'][c] += 1
                    
                elif planets[p[0]]['pos'][c] < planets[p[1]]['pos'][c]:
                    planets[p[0]]['vel'][c] += 1
                    planets[p[1]]['vel'][c] -= 1
        sumVelToPos(planets)
        if p2:
            if len(found) != 3:
                for c in COORDS:
                    h = hashPlanets(planets, c)
                    if h in hashes[c] and c not in found:
                        print("planets have the same pos and vol at step {} for {}".format(s, c))
                        cords[c] = s
                        found.add(c)
                    else:
                        hashes[c].add(h)
            else:
                return cords


def main():
    data = getInts('input')

    planets = list()
    i = 0
    for planet in data:
        a = {}
        a['pos'] = dict(zip(['x','y','z'], planet ))
        a['vel'] = {'x':0, 'y':0, 'z':0}
        a['id'] = i
        planets.append( a )
        i+= 1

    pairs = list(combinations(range(len(planets)), 2))

    planets2 = planets.copy()

    # part 1
    simulation(planets, pairs, 1000)
    p1 = sum([ getEnergy(x) for x in planets ])
    print("p1: {}".format(p1))


    # part 2 
    p2_s = simulation(planets2, pairs, 9999999999, True)
    p2 = lcm.reduce([x for x in p2_s.values()])
    print("p2: {}".format(p2))
    


if __name__ == '__main__':
    main()