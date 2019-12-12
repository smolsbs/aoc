#!/usr/bin/env python3

import AoCUtils

def main():
    data = AoCUtils.loadInput('input')

    asteroidField = []
    
    for line in data:
        aux = [1 if c == '#' else 0 for c in line]
        asteroidField.append(aux)
    (max_x, max_y) = len(asteroidField[0]), len(asteroidField)

    print(asteroidField)
    print(max_x, max_y)


if __name__ == '__main__':
    main()