#!/usr/bin/env python3

from re import sub
def check_ch(a, b):
    if a.lower() == b.lower():
        if (a.isupper() and b.islower()) or (a.islower() and b.isupper()):
            return True
        return False

def reactor(data):
    newdata = ""
    for ch in data:
        if  newdata != "" and check_ch(ch, newdata[-1]):
            newdata = newdata[:-1]
        else:
            newdata += ch

    return len(newdata)

def main():
    with open('../input', 'r') as fp:
        data = fp.read().strip('\n')

    part1 = reactor(data)
    print(part1)
    abc = 'abcdefghijklmnopqrstuvwxyz'

    part2 = []
    for ch in abc:
        pat = r'(%c|%c)' % (ch, ch.upper())
        part2.append(reactor(sub(pat, '', data)))

    print(part1)
    print(min(part2))


if __name__ == '__main__':
    main()
