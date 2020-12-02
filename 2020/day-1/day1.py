#!/usr/bin/env python3
def main():
    with open('input', 'r') as fp:
        data = {int(x) for x in fp.readlines()}
    
    # O(n)
    for i in data:
        # subtract i from 2020 and see if it's in data
        v = 2020 - i
        if v in data:
            print("part 1: {}".format(v*i))
            break
    
    # O(n^2)
    for v1 in data:
        for v2 in data:
            v3 = 2020 - (v1+v2)
            if v3 in data:
                print("part 2: {}".format(v1*v2*v3))
                return


if __name__ == '__main__':
    main()