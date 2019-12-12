#!/usr/bin/env python3

from AoCUtils import getInts

DEF = {'x':None, 'y':None, 'Z':None}
COORDS = {'x', 'y', 'z'}

def sumVelToPos(planets):
    for p in planets:
        for v in COORDS:
            p['pos'][v] += p['vel'][v]


def simulation(data):
    pass

def main():
    data = getInts('input')

    planets = []
    i = 0
    for planet in data:
        a = {}
        a['pos'] = dict(zip(['x','y','z'], planet ))
        a['vel'] = {'x':0, 'y':0, 'z':0}
        a['id'] = i
        planets.append( a )
        i+= 1

    sumVelToPos(planets) 
    print(planets)

if __name__ == '__main__':
    main()