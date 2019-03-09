#!/usr/bin/python

KEYPAD = [[1,2,3], [4,5,6], [7,8,9]]
KP =  [[None, None, 1, None, None],
[None, 2, 3, 4, None],
[5, 6, 7, 8, 9],
[None, 'A', 'B', 'C', None],
[None, None, 'D', None, None]]

def part1(number):
    code = ''
    pos  = [1, 1] # x, y
    for line in number:
        for c in line:
            if c == 'U':
                pos[1] = max(0, pos[1] - 1)
            elif c == 'R':
              pos[0] = min(2, pos[0] + 1)
            elif c == 'D':
                pos[1] = min(2, pos[1] + 1)
            elif c == 'L':
                pos[0] = max(0, pos[0] - 1)
        code += str(KEYPAD[pos[1]][pos[0]])
    print(code)

def part2(number):
    code = ''
    pos  = [0, 2] # x, y
    for line in number:
        for c in line:
            if c == 'U':
                newPos = [pos[0], max(0, pos[1] - 1)]
            elif c == 'R':
              newPos = [min(4, pos[0] + 1), pos[1]]
            elif c == 'D':
                newPos = [pos[0], min(4, pos[1] + 1)]
            elif c == 'L':
                newPos = [max(0, pos[0] - 1), pos[1]]
            if KP[newPos[1]][newPos[0]] is not None:
                pos = newPos
        code += str(KP[pos[1]][pos[0]])
    print(code)


def main():
    with open('input', 'r') as fp:
        number = [line for line in fp.read().strip().split('\n')]
    
    part1(number)
    part2(number)



if __name__ == '__main__':
    main()