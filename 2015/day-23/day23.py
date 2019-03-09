#!/usr/bin/python

def parseInst(_string):
    aux = _string.strip().split(' ')
    if len(aux) == 2:
        return aux
    else:
        aux[1] = aux[1][0]
        return aux


class Interpreter:
    def __init__(self, codes, p2=False):
        self.program = codes
        self.reg = {'a':0, 'b':0}
        if p2:
            self.reg['a'] = 1
        self.ip = 0
        self.max = len(self.program)
        self.opset = {'hlf':self.hlf, 
                    'tpl':self.tpl, 
                    'inc':self.inc,
                    'jmp':self.jmp, 
                    'jie':self.jie, 
                    'jio':self.jio}

    def hlf(self, r):
        self.reg[r] //= 2
        self.ip += 1
    
    def tpl(self, r):
        self.reg[r] *= 3
        self.ip +=1
    
    def inc(self, r):
        self.reg[r] += 1
        self.ip +=1

    def jmp(self, off):
        self.ip += int(off)

    def jie(self, r, off):
        if self.reg[r] % 2 == 0:
            self.ip += int(off)
        else:
            self.ip += 1
    def jio(self, r, off):
        if self.reg[r] == 1:
            self.ip += int(off)
        else:
            self.ip += 1

    def run(self):
        while self.ip < self.max and self.ip >= 0:
            inst = self.program[self.ip]
            if len(inst) == 2:
                self.opset[inst[0]](inst[1])
            else:
                self.opset[inst[0]](inst[1], inst[2])
        return self.reg['b']


if __name__ == '__main__':
    with open('input', 'r') as fp:
        code = [parseInst(x) for x in fp.readlines()]

    # swap commented lines for part 2
    PC = Interpreter(code)
    # PC = Interpreter(code, True) 
    print(PC.run())
