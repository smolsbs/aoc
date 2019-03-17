#!/usr/bin/python
from re import findall
import numpy as np

def actOn(array, a):
    if len(a) == 2:
        array[0:a[0], 0:a[1]] = np.ones(a, dtype='int')
    else:
        if a[0] == 'r':
            array[a[1], :] = np.roll(array[a[1], :], a[2])
        else:
            array[:, a[1]] = np.roll(array[:, a[1]], a[2])

    return array

def main():
    screen = np.zeros((6,50), dtype='int')
    with open('input') as fp:
        for line in fp.read().strip().split('\n'):
            n1, n2 = map(int, findall(r'\d+',line))
            aux = line.split(' ')
            if len(aux) == 2:
                screen = actOn(screen, (n2, n1))   # get rect size, n1=y, n2=x
            else:
                if aux[1] == 'row':
                    screen = actOn(screen, ('r', n1, n2))
                else:
                    screen = actOn(screen, ('r', n1, n2))

    # part 1
    print(np.sum(screen))

    # part 2
    for line in screen:
        print(''.join(['#' if c == 1 else ' ' for c in list(line)]))

if __name__ == '__main__':
    main()