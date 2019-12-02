#!/usr/bin/env python3
import AoCUtils

def Machine(intcode, value1, value2):
    intcode = intcode.copy()
    intcode[1] = value1
    intcode[2] = value2
    ip = 0
    while True:
        opcode = intcode[ip]
        if opcode == 99:
            break
        else:
            valA_add = intcode[ip+1] 
            valB_add = intcode[ip+2]
            store_add = intcode[ip+3]

            if opcode == 1:
                intcode[store_add] = int(intcode[valA_add] + intcode[valB_add])
            if opcode == 2:
                intcode[store_add] = int(intcode[valA_add] * intcode[valB_add])

        ip += 4
    return intcode[0]


def main():
    data = AoCUtils.loadInput('input')
    data = list(map(int, data[0].split(',')))

    # part 1 input
    print(Machine(data, 12, 2))

    # part 2
    for noun in range(0, 100):
        for verb in range(0, 100):
            if Machine(data, noun, verb) == 19690720:
                print("{}".format(100*noun+verb))


if __name__ == '__main__':
    main()