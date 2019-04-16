#! python

from math import sqrt, ceil
def main():
    with open('input') as fp:
        data = int(fp.read().strip())

    # each square of memory is (2n+1)^2 of storage space
    # So, find the upper n that is above the input number

    c = ceil(sqrt(data)) - 1 // 2
    print(c)

if __name__ == '__main__':
    main()