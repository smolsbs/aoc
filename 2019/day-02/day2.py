#!/usr/bin/env python3
import AoCUtils

def Machine(intcode, value1, value2):
    intcode = intcode.copy()
    intcode[1] = value1
    intcode[2] = value2
    ip = 0
    while True:
        opcode = intcode[ip]
        if opcode == 99: break
        (pA, pB, rA) = intcode[ip+1 : ip+4]
        if opcode == 1:
            intcode[rA] = intcode[pA] + intcode[pB]
        if opcode == 2:
            intcode[rA] = intcode[pA] * intcode[pB]

        ip += 4
    return intcode[0]


def main():
    data = list(map(int, AoCUtils.loadInput('input')[0].split(',')))

    # part 1 input
    print(Machine(data, 12, 2))

    # part 2
    for noun in range(0, 100):
        for verb in range(0, 100):
            if Machine(data, noun, verb) == 19690720:
                print("{}".format(100*noun+verb))


if __name__ == '__main__':
    main()