#!/usr/bin/env python3
from re import findall

class Instrucs:
    @staticmethod
    def acc(ip, val, reg):
        return (ip+1, reg + val)
    
    @staticmethod
    def jmp(ip, val, reg):
        return (ip+val, reg)
    
    @staticmethod
    def nop(ip, val, reg):
        return (ip + 1, reg)

INSTRUCS = {'acc': Instrucs().acc, 'jmp': Instrucs().jmp, 'nop': Instrucs().nop}

def run(data):
    n_instructs = len(data)
    ip = 0 
    reg = 0
    visited_ip = [0]

    while ip < n_instructs:
        code, val = data[ip]
        # actual instruction being done here
        ip, reg = INSTRUCS[code](ip, val, reg)
        if ip in visited_ip:
            return (-1, reg)
        visited_ip.append(ip)

    return (0, reg)


def main():
    with open('input', 'r') as fp:
        data = []
        jmp_nop_pos = []        # part 2
        pos = 0                 # part 2
        for x in fp.read().split('\n'):
            if x == "":
                break
            opcode, arg = findall(r'(\w{3}) (\+\d+|\-\d+)', x)[0]

            # for part 2
            if opcode == 'jmp' or opcode == 'nop':
                jmp_nop_pos.append(pos)

            data.append( (opcode, int(arg)) )
            pos += 1            # part 2

    # part 1
    status, val = run(data)
    print("part 1: %d" % val)

    # part 2
    for ici in jmp_nop_pos:
        new_data = data.copy()

        if new_data[ici][0] == 'jmp':
            new_data[ici] = ('nop', new_data[ici][1])
        else:
            new_data[ici] = ('jmp', new_data[ici][1])

        status, val = run(new_data)
        if status == 0:
            break
    print('part 2: %d' % val)


if __name__ == '__main__':
    main()