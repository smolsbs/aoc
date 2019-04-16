#!/usr/bin/env python3

# (2 3 {0 3 10 11 12} {1 1 [0 1 99] 2} 1 1 2)
# Specifically, a node consists of:

# A header, which is always exactly two numbers:
# - The quantity of child nodes.
# - The quantity of metadata entries.
# - Zero or more child nodes (as specified in the header).
# - One or more metadata entries (as specified in the header).

def parser(data):
    nChildren = data.pop(0)
    nMetadata = data.pop(0)
    checksum = []
    value = []

    for _ in range(nChildren):
        aux, data = parser(data)
        checksum += aux
    
    if nChildren == 0:
        for _ in range(nMetadata):
            meta = data.pop(0)
            checksum.append(meta)

    else:
        for _ in range(nMetadata):
            meta = data.pop(0)
            # print(meta)
            checksum.append(meta)
    
    if len(data) == None:
        return checksum
    return checksum, data



def main():
    # fp = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    # data = list(map(int, fp.split(' ')))
    with open('input', 'r') as fp:
        data = list(map(int, fp.read().strip().split(' ')))

    a = parser(data)

    print(sum(a[0]))
        


if __name__ == '__main__':
    main()