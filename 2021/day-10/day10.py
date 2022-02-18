#!/usr/bin/env python3

import aocUtils

PTS_INV = {')': 3, ']': 57, '}': 1197, '>': 25137}
PTS_INC = {')': 1, ']': 2, '}': 3, '>': 4}
PAIRS = {'(':')', '[': ']', '{':'}', '<':'>'}

def syntax_scoring(_syntax, pts_1, pts_2):
    """Go through _syntax and do the following things:
    - If an opening chunk, store it into queue;
    - If a closing chunk, compare if it's the pair to the last
    item in the queue.
        - if true, remove opening chunck from queue
        - if false, set invalid to True, and add to pts_1 the value on PTS_INV

    - If after going through the string, the queue is not emtpy, create the remaing chunks,
    calculate the appropiate points for them and append to pts_2.

    Args:
        _syntax (str): line to check syntax
        pts_1 (int): accumulated value for part 1
        pts_2 (list): list of points for all incomplete string

    Returns:
        tuple: pts_1 and pts_2
    """
    if len(_syntax) == 0:
        return pts_1, pts_2

    opens = set(PAIRS.keys())
    closes = set(PAIRS.values())

    queue = []
    invalid = False

    for _c in _syntax:
        if _c in opens:
            queue.append(_c)
        elif _c in closes:
            if _c == PAIRS[queue[-1]]:
                queue.pop(-1)
            else:
                pts_1 += PTS_INV[_c]
                invalid = True
                break

    if len(queue) != 0 and not invalid:
        rem_vals = [PAIRS[x] for x in queue[::-1]]
        _p2 = 0
        for _c in rem_vals:
            _p2 *= 5
            _p2 += PTS_INC[_c]
        pts_2.append(_p2)

    return pts_1, pts_2


def main():
    """Main routine"""
    data = aocUtils.loadInput('input')

    _p1 = 0
    _p2 = []
    for line in data:
        _p1, _p2 = syntax_scoring(line, _p1, _p2)

    _p2 = sorted(_p2)[len(_p2)//2]

    print(f'part1: {_p1}')
    print(f'part2: {_p2}')

if __name__ == '__main__':
    main()
