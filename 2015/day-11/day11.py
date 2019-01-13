#!/usr/bin/env python3
import sys
from itertools import groupby
def checks(pw):
    conseq = False
    pairs = 0
    for c in range(5):     # requirement 1
        if ord(pw[c]) == ord(pw[c+1]) + 1 and ord(pw[c]) == ord(pw[c+2]) + 2:
            conseq = True
    if conseq is False:
        return False
    # print("\tReq 1 pass")

    for _, g in groupby(pw):  # requirement 3
        if len(list(g)) == 2:
            pairs += 1
    if pairs < 2:
        return False
    # print("\tReq 3 pass")
    return True

def next_char(char):
    c = (ord(char) - ord('a') + 1) % 26
    if c == 0:
        return ('a', True)
    return (chr(c + ord('a')), False)

def main():
    password = list(sys.argv[1])[::-1]
    i = 1
    while True:
        index = 0
        overflow = False
        password[index], overflow = next_char(password[index])
        while overflow:
            index += 1
            password[index], overflow = next_char(password[index])
        for b in ["i", "l", "o"]:       # requirement 2
            if b in password:
                i += 1
                continue
        if checks(password):
            print("New password: {}\nNumber of iterations: {}".format(''.join(password[::-1]), i))
            break
        i += 1

    
if __name__ == '__main__':
    main()