#!/usr/bin/env python3

from math import ceil, floor

def mid(a, b, mode):
    if mode:
        return ceil( (a+b) / 2 )
    else:
        return floor( (a+b) / 2 )

def get_seat(b_pass):
    row, seat = (0,0)
    b = [0,127]
    s = [0, 7]
    for i in range(7):
        if b_pass[0][i] == 'B':
            b[0] = mid(b[0], b[1], 1)
        else:
            b[1] = mid(b[0], b[1], 0)
    if b_pass[0][6] == 'B':
        row = b[1]
    else:
        row = b[0]
    
    for j in range(3):
        if b_pass[1][j] == 'R':
            s[0] = mid(s[0], s[1], 1)
        else:
            s[1] = mid(s[0], s[1], 0)
    if b_pass[1][2] == 'R':
        seat = s[1]
    else:
        seat = s[0]
    
    return (row * 8) + seat

def main():
    with open('input', 'r') as fp:
        data = [ (x[:7], x[7:]) for x in fp.read().split('\n')]
    
    sid = set()

    for p in data:
        sid.add(get_seat(p))

    print(sorted(sid, reverse=True)[0])


if __name__ == '__main__':
    main()