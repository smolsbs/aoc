#! python

from re import findall
from itertools import combinations

def main():
    with open('input') as fp:
        data = fp.read().strip().split('\n')
    chsum = 0
    chsum_2 = 0
    for line in data:
        # part 1
        numbs = sorted(list(map(int, line.split('\t'))), reverse=True)
        chsum += (numbs[0] - numbs[-1])

        # part 2
        nCombs = combinations(numbs, 2)
        for c in nCombs:
            if c[0] % c[1] == 0:
                chsum_2 += c[0] // c[1]


    print(chsum)
    print(chsum_2)

if __name__ == '__main__':
    main()