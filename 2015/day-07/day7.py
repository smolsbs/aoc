#!/usr/bin/env python3
import sys
from collections import defaultdict
import operator as op

OPS = {"LSHIFT": op.lshift,
        "RSHIFT": op.rshift,
        "AND": op.and_,
        "OR": op.or_}

def op_equ(value):
    return value

def op_not(value):
    return 0xffff - value

def getOp(op):
    return OPS[op]

def memoize(f):
    memo = {}
    def checkMemo(queue, wire):
        if wire not in memo:
            memo[wire] = f(queue, wire)
        return memo[wire]
    return checkMemo

@memoize
def find_wire(queue, wire):
    try:
        return int(wire)
    except ValueError:
        pass
    val = queue[wire]
    if len(val) == 2:
        return val[0](find_wire(queue, val[1]))
    else:
        return val[0](find_wire(queue, val[1]), find_wire(queue, val[2]) )

def main():
    queue = defaultdict(list)

    if len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        fname = 'input'
    with open(fname, 'r') as fp:
        for line in fp.read().split('\n'):
            a = line.split()
            if len(a) == 3:
                queue[a[-1]] = (op_equ, a[0])
            elif len(a) == 4:
                queue[a[-1]] = (op_not, a[1])
            else:
                queue[a[-1]] = (getOp(a[1]), a[0], a[2])

    val = find_wire(queue, 'a')
    print(val)

if __name__ == '__main__':
    main()

