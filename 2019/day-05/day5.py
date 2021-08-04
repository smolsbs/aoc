#!/usr/bin/env python3

import AoCUtils
import time

class IntMachine:
    def __init__(self, intcode):
        self._intcode = list(map(int, intcode.copy()))
        self._ip = 0
        self._continue = True
        self._opcodes = {1:self.add, 2:self.mul, 3:self.store, 4:self.ret,
                         5:self.jit, 6:self.jif, 7:self.le, 8:self.eq}
        self._return = None

    def reset(self, intcode):
        self._intcode = list(map(int, intcode.copy()))
        self._ip = 0
        self._continue = True


    def run(self, id):
        self._id = id
        while self._continue:
            aux = '{:05d}'.format(self._intcode[self._ip])
            self.opcode = int(aux[3:])
            self.modeA = int(aux[2])
            self.modeB = int(aux[1])
            self.modeC = int(aux[0])

            if self.opcode in [1,2,7,8]:
                (a,b,c) = self._intcode[self._ip+1:self._ip+4]
                self._opcodes[self.opcode](a,b,c)

            elif self.opcode in [3,4]:
                a = self._intcode[self._ip+1]
                self._opcodes[self.opcode](a)

            elif self.opcode in [5,6]:
                (a,b) = self._intcode[self._ip+1:self._ip+3]
                self._opcodes[self.opcode](a,b)

            elif self.opcode == 99:
                self.quit()
        
        return self._return

    def quit(self):
        self._continue = False

    def getMode(self, param, mode):

        if mode == 1:
            return self._intcode[self._ip+param]
        return self._intcode[self._intcode[self._ip+param]]

    def add(self, pA, pB, rA):      # opcode 1        
        self._intcode[rA] = self.getMode(1, self.modeA) + self.getMode(2, self.modeB)
        self._ip += 4
    
    def mul(self, pA, pB, rA):      # opcode 2
        self._intcode[rA] = self.getMode(1, self.modeA) * self.getMode(2, self.modeB)
        self._ip += 4

    def store(self, rA):            # opcode 3
        self._intcode[rA] = self._id
        self._ip += 2

    def ret(self, pA):              # opcode 4
        if self.getMode(1, self.modeA) != 0:
            self._return = self.getMode(1, self.modeA)
            # print(self.getMode(1, self.modeA))
        self._ip += 2
    
    def jit(self, pA, pB):          # opcode 5
        if self.getMode(1, self.modeA) != 0:
            self._ip = self.getMode(2, self.modeB)
            return
        self._ip += 3

    def jif(self, pA, rA):          # opcode 6
        if self.getMode(1, self.modeA) == 0:
            self._ip = self.getMode(2, self.modeB)
            return
        self._ip += 3

    def le(self, pA, pB, rA):
        if self.getMode(1, self.modeA) < self.getMode(2, self.modeB):
            self._intcode[rA] = 1
        else:
            self._intcode[rA] = 0
        self._ip += 4

    def eq(self, pA, pB, rA):
        if self.getMode(1, self.modeA) == self.getMode(2, self.modeB):
            self._intcode[rA] = 1
        else:
            self._intcode[rA] = 0
        self._ip += 4

def main():
    data = AoCUtils.loadInput('input')[0].split(',')
    start = time.time_ns()

    a = IntMachine(data)
    print("part1: ", a.run(1))
    a.reset(data)
    print("part2: ", a.run(5))

    print("{}ms".format((time.time_ns() - start)/10**6 ))
if __name__ == '__main__':
    main()