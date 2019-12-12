#!/usr/bin/env python3

import AoCUtils
from itertools import permutations

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

    def soft_reset(self):
        self._ip = 0
        self._continue = True

    def run(self, signals):
        self._signals = signals
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
        if len(self._signals) != 0:
            self._intcode[rA] = self._signals.pop(0)
        else:
            self._intcode[rA] = self._return
        self._ip += 2

    def ret(self, pA):              # opcode 4
        self._return = self.getMode(1, self.modeA)
        self._id = self._return
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


def run(intcode, signals, part2=False):
    totals = []
    software = IntMachine(intcode)
    for signal in signals:
        s = 0
        for i in signal:
            aux = [i,s]
            s = software.run(aux)
            if part2:
                software.soft_reset() 
            else:    
                software.reset(intcode)        
        totals.append(s)
    
    return sorted(totals, reverse=True)[0]


def main():
    data = AoCUtils.loadInput('input')[0].split(',')

    p1_signals = permutations(range(5),5)
    # p2_signals = permutations(range(5,10),5)

    p1 = run(data, p1_signals)
    # p2 = run(data, p2_signals, True)
    
    print(p1)
    # print(p2)

if __name__ == '__main__':
    main()