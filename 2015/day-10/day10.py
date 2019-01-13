#!/usr/bin/env python3
from itertools import groupby
def main():
    inp = "1113122113"

    for _ in range(50):
        newinp = ""
        for k, g in groupby(inp):
            newinp += str(len(list(g))) + k
        inp = newinp
        if _ == 39:
            print(len(inp))
    print(len(inp))
if __name__ == '__main__':
    main()
