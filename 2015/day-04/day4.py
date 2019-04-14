#!/usr/bin/env python3
#
import hashlib

def thing(secret, part2=False):
    i = 10000
    while True:
        text = secret + str(i)

        hashed = hashlib.md5(bytes(text, 'utf-8')).hexdigest()

        if part2:
            if hashed[:6] == '000000':
                return text, hashed
        else:
            if hashed[:5] == '00000':
                return text, hashed
        i +=1 

def main():
    with open('input') as fp:
        secret = fp.read().strip()
    print(thing(secret))
    print(thing(secret, True))
    


if __name__ == '__main__':
    main()