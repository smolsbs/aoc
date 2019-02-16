#!/usr/bin/python
from PIL import Image, ImageDraw

def createFrame(grid):
    img = Image.new('RGB', (100, 100), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    q = []
    for line in range(100):
        for elem in range(100):
            if grid[line][elem] == 1:
                q.append((elem, line))
    draw.point(q, (255, 255, 255))
    return img


def sumNeighbours(x, y, grid):
    if y == 0:
        if x == 0:
            return sum(grid[y][x:x+2]) + sum(grid[y+1][x:x+2]) - grid[y][x]
        else:
            return sum(grid[y][x-1:x+2]) + sum(grid[y+1][x-1:x+2]) - grid[y][x]
    elif y == 99:
        if x == 0:
            return sum(grid[y-1][x:x+2]) + sum(grid[y][x:x+2]) - grid[y][x]
        else:
            return sum(grid[y-1][x-1:x+2]) + sum(grid[y][x-1:x+2]) - grid[y][x]
    else:
        return sum(grid[y-1][x-1:x+2]) + sum(grid[y][x-1:x+2]) + sum(grid[y+1][x-1:x+2]) - grid[y][x]


def processLights(grid):
    frames = []
    newGrid = grid
    for _ in range(100):
        for line in range(100):
            for row in range(100):
                s = sumNeighbours(row, line, grid)

                if grid[line][row] == 1:
                    if s not in [2,3]:
                        newGrid[line][row] == 0
                elif grid[line][row] == 0:
                    if s == 3:
                        newGrid[line][row] == 1

        grid = newGrid
        frames.append(createFrame(grid))
        print("frame {} done".format(_+1))
    return (grid, frames)


def main():
    grid = []
    with open('input', 'r') as fp:
        for line in fp.read().split('\n'):
            grid.append([1 if x == '#' else 0 for x in line])

    final, frames = processLights(grid)

    frames[0].save('a.png', format='PNG')
    frames[98].save('b.png', format='PNG')


if __name__ == '__main__':
    main()