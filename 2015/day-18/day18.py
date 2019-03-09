#!/usr/bin/python

def strToInt(c):
    if c == '#':
        return 1
    else:
        return 0
    

def getArround(grid, i, j):
    state = 0
    # print("%d %d" % (i, j))
    for x in range(max(0, i-1), min(len(grid), i+2)):
        # l = ''
        for y in range(max(0, j-1), min(len(grid), j+2)):
            # l += str(grid[x][y])
            state += grid[x][y]
        # print(l)
    return state - grid[i][j]


def main():
    grid = []
    with open('input', 'r') as fp:
        for line in fp.read().split('\n'):
            grid.append([strToInt(c) for c in line])
    gridLen = len(grid)
    frame = 0
    
    while frame < 100:
        newGrid = [[0 for _ in range(gridLen)] for _ in range(gridLen)]
        for x in range(gridLen):
            for y in range(gridLen):
                s = getArround(grid, x, y)
                if (s == 2 or s == 3) and grid[x][y] == 1:
                    newGrid[x][y] = 1
                elif s == 3 and grid[x][y] == 0:
                    newGrid[x][y] = 1
                # enable this condition for part 2
                # elif (x,y) in [(0,0), (0, gridLen-1), (gridLen-1, 0), (gridLen-1, gridLen-1)]:
                #     newGrid[x][y] = 1
                else:
                    newGrid[x][y] = 0
        grid = newGrid
        frame += 1

    total = 0
    for line in grid:
        total += sum(line)

    print(total)

if __name__ == '__main__':
    main()
