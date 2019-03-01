#!/usr/bin/python

def animate(grid, n, frames):
    _grid = grid
    newGrid = [[0 for _ in range(n)] for _ in range(n)]
    frame = 0
    while(frame < frames):
        for i in range(n):
            for j in range(n):
                value = getNeighbours(_grid, i, j)     
                if _grid[i][j] == 1:
                    if value == 2 or value == 3:
                        newGrid[i][j] = 1
                elif _grid[i][j] == 0:
                    if value == 3:
                        newGrid[i][j] = 1
        _grid = newGrid
        frame += 1

    return _grid


def getNeighbours(grid, i, j, dist=1):
    value = 0

    for line in grid[max(0, i-dist):i+dist+1]:
        for e in line[max(0, j-dist):j+dist+1]:
            value += e

    return value - grid[i][j]


def main():
    grid = []
    with open('input', 'r') as fp:
        for line in fp.read().split('\n'):
            a = []
            for c in line:
                if c == "#":
                    a.append(1)
                else:
                    a.append(0)
            grid.append(a)
    
    newGrid = animate(grid, len(grid), 100)
    
    total = 0

    for x in range(len(newGrid)):
        total += sum(newGrid[x])
    print(total)

if __name__ == '__main__':
    main()
