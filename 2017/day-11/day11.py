#! python
from math import floor, ceil


def sign(n):
    if n >= 0:
        return True
    else:
        return False


compass = {'n': (0, 1), 's': (0, -1), 'e': (1, 0), 'w': (-1, 0),
            'ne': (1, 1), 'nw': (-1, 1), 'se': (1, -1), 'sw': (-1,-1)
}


def runSteps(steps):
    x, y = (0, 0)
    for step in steps:
        a , b = compass[step]
        x += a
        y += b
    
    return (x, y)

def hexManhattan(x, y):
    dx = x - floor(y/2)
    dy = y - ceil(y/2)


    if sign(dx) == sign(dy):
        return abs(dx + dy)
    else:
        return max(abs(dx), abs(dy))

    

def main():
    with open('input') as fp:
        data = list(fp.read().strip().split(','))

    dx, dy = runSteps(data)
    print(hexManhattan(dx, dy))


if __name__ == '__main__':
    main()