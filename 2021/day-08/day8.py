#!/usr/bin/env python3

import aocUtils

def decode_segs(_signals: list) -> dict:
    true_sig = {k:None for k in range(10)}
    segs_6 = [x for x in _signals if len(x) == 6]
    segs_5 = [x for x in _signals if len(x) == 5]

    # get the unique numbers
    for number in _signals:
        if len(number) == 2:
            true_sig[1] = number
        if len(number) == 3:
            true_sig[7] = number
        if len(number) == 4:
            true_sig[4] = number
        if len(number) == 7:
            true_sig[8] = number
    # seg 3 has seg 1 as it's subset
    for i in segs_5:
        if set(true_sig[1]).issubset(set(i)):
            true_sig[3] = i
            segs_5.remove(i)
            break
    # seg 9 has seg 4 as it's subset
    for i in segs_6:
        if set(true_sig[4]).issubset(set(i)):
            true_sig[9] = i
            segs_6.remove(i)
            break
    # seg 0 has seg 1 as it's subset. this also gives us 6
    for i in segs_6:
        if set(true_sig[1]).issubset(set(i)):
            true_sig[0] = i
            segs_6.remove(i)
            break
    true_sig[6] = segs_6.pop()
    #finally, seg 5 is a subset of seg 6, while seg 2 is not
    for i in segs_5:
        if set(i).issubset(set(true_sig[6])):
            true_sig[5] = i
            segs_5.remove(i)
            break
    true_sig[2] = segs_5.pop()

    return true_sig

def part1(_outputs: list):
    unique = 0
    for l in _outputs:
        for sign in l:
            if len(sign) in {2, 3, 4, 7}:
                unique += 1
    return unique

def part2(_signals: list, _outputs: list):
    _sum = 0
    for signal, output in zip(_signals, _outputs):
        true_sig = decode_segs(signal)
        out = [x for x in output]
        aux = ''
        for o in out:
            for k, v in true_sig.items():
                if set(v) == set(o):
                    aux += str(k)
                    break
        _sum += int(aux)
    
    return _sum


def main():
    signals = []
    output = []

    with open('input') as fp:
        for l in fp.read().strip().split('\n'):
            aux = l.split(' | ')
            signals.append([x for x in aux[0].split(' ')])
            output.append([x for x in aux[1].split(' ')])

    p1 = part1(output)
    p2 = part2(signals, output)

    print(f'part1: {p1}')
    print(f'part2: {p2}')

if __name__ == '__main__':
    main()