#!/usr/bin/env python3
from random import choice
import time
import AoCUtils

def Machine(intcode, value1, value2, verbose=False):
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
    # print(Machine(data, 12, 2))
    # part 2
    sdf = []
    sr = []
    N_ATTEMPTS = 200
    print("Number of runs for each method:{}".format(N_ATTEMPTS))
    print("{}\nTesting double for".format('='*20))
    for _ in range(N_ATTEMPTS):
        if _ % 10 == 0: print("run: {}".format(_))
        br = False
        start = time.time()
        while not br:
            for noun in range(0, 100):
                for verb in range(0, 100):
                    if Machine(data, noun, verb) == 19690720:
                        stop = time.time()
                        br = True

        sdf.append(round((stop - start)*100, 8))

    a = [x for x in range(0, 100)]
    print("{}\nTesting random".format('='*20))
    for _ in range(N_ATTEMPTS):
        if _ % 10 == 0: print("run: {}".format(_))
        br = False
        start = time.time()
        while not br:
            if Machine(data, choice(a), choice(a)) == 19690720:
                stop = time.time()
                br = True
        sr.append(round((stop - start)*100, 8))      
    
    from statistics import stdev
    sdf = sorted(sdf)
    sr = sorted(sr)
    print("\n{}\n".format('='*20))
    print("RESULTS\n")
    print("Double for loop:")
    print("\tAverage: {}ms".format(sum(sdf)/N_ATTEMPTS))
    print("\tBest run: {}ms".format(sdf[0]))
    print("\tWorst run: {}ms".format(sdf[-1]))
    print("Standart deviation: {}ms".format(stdev(sdf)))
    print("\n{}\n".format('='*20))
    print("Random choices:")
    print("\tAverage: {}ms".format(sum(sr)/N_ATTEMPTS))
    print("\tBest run: {}ms".format(sr[0]))
    print("\tWorst run: {}ms".format(sr[-1]))
    print("Standart deviation: {}ms".format(stdev(sr)))




if __name__ == '__main__':
    main()