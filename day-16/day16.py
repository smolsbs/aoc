#!/usr/bin/env python3
def parse(lyst):
    before = []
    instr = []
    after = []
    for i in range(0, len(lyst), 4):
        before.append(tuple(lyst[i][8:-1].split(', ')))
        instr.append(tuple(lyst[i+1].split(' ')))
        after.append(tuple(lyst[i+2][8:-1].split(', ')))
    return (before, instr, after)


def main():

    with open('sinput', 'r') as fp:
    # with open('input', 'r') as fp:
        before, instr, after = parse(fp.read().split('\n'))





class Opcodes():
    def __init__(self):
        opcode = 
        reg1 = None
        reg2 = None
        reg3 = None
        val = None
    
    def addr(self):
        self.val = self.reg1 + self.reg2
        return self.val

    def addi(self):
        self.val += self.reg2
    
    def mulr(self):
        self.val = self.reg1 * self.reg2
        return self.val
    def 
    


if __name__ == '__main__':
    main()