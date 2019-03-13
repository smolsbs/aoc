#!/usr/bin/python

from re import findall
import numpy as np

def actOn(array, act):
    if len(act) == 2:
        array[0:act[1], 0:act[0]] = np.ones((act[1],act[0]), dtype='int')
    elif len(act) == 3:
        if act[0] == 'r':
            array[act[1], :] = np.roll(array[act[1], :], act[2])
        else:
            array[:, act[1]] = np.roll(array[:, act[1]], act[2])

    return array

def printLine(line):
    print(''.join(['#' if c == 1 else ' ' for c in list(line)]))

def main():
    actions = []
    screen = np.zeros((6,50), dtype='int')
    with open('input') as fp:
        for line in fp.read().strip().split('\n'):
            n1, n2 = map(int, findall(r'\d+',line))
            aux = line.split(' ')
            if len(aux) == 2:
                actions.append( (n1, n2) )   # get rect size, n1=y, n2=x
            else:
                if aux[1] == 'row':
                    actions.append( ('r', n1, n2) )
                else:
                     actions.append( ('c', n1, n2) )
    for action in actions:
        screen = actOn(screen, action)

    print(np.sum(screen))

    for line in screen:

        printLine(line)

if __name__ == '__main__':
    main()