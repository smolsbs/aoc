#!/usr/bin/env python3

from math import sqrt
import aocUtils


MVMNT = {'U': (1,0), 'D': (-1,0), 'L': (0, -1), 'R': (0,1)}
ROOT_2 = sqrt(2)
X = 1
Y = 0


class Rope:
    def __init__(self):
        self.parts = [[0,0] for _ in range(10)]
        self.visited_p1 = {(0,0)}
        self.visited_p2 = {(0,0)}

    def move(self, action, amt):
        mv = MVMNT[action]
        for _ in range(amt):
            self.parts[0][X] += mv[X]
            self.parts[0][Y] += mv[Y]
            for idx in range(1, len(self.parts)):
                att, c = is_attached(self.parts[idx-1], self.parts[idx])
                if not att:
                    self.parts[idx][X] = self.parts[idx-1][X] - c[X]
                    self.parts[idx][Y] = self.parts[idx-1][Y] - c[Y]

            self.visited_p1.add( (self.parts[1][Y], self.parts[1][X]) )
            self.visited_p2.add( (self.parts[-1][Y], self.parts[-1][X]) )

    def get_visited(self):
        return len(self.visited_p1), len(self.visited_p2)


def is_attached(x1,x2):
    d = sqrt(abs((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2))
    if d > ROOT_2:
        d_x = x1[X]-x2[X]
        d_y = x1[Y]-x2[Y]
        correction = [0,0]
        if d_x < 0:
            correction[X] = d_x+1
        elif d_x > 0:
            correction[X] = d_x-1
        if d_y < 0:
            correction[Y] = d_y+1
        elif d_y > 0:
            correction[Y] = d_y-1
        return False, correction
    return True, None

def solve(data):
    rope = Rope()
    for line in data:
        action, amt = line.split(' ')

        rope.move(action, int(amt))

    return rope.get_visited()

def run(path):
    data = aocUtils.loadInput(f"{path}/input")
    return solve(data)
