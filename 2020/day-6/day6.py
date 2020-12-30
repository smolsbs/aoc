#!/usr/bin/env python3

from collections import Counter 

def main():
    with open('input', 'r') as fp:
        part1 = 0
        part2 = 0
        for p in fp.read().split('\n\n'):
            answers = list(p.split('\n'))
            n_members = len(answers)

            all_answers = ''.join(answers)
            aux = Counter(all_answers)

            # part 1
            part1 += len(aux.keys())

            # part 2
            all_same = list(filter(lambda x: aux[x] == n_members, aux ))
            part2 += len(all_same)

    print('part1: %d' % part1)
    print('part2: %d' % part2)
if __name__ == '__main__':
    main()