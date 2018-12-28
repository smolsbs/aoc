#!/usr/bin/env python3
#
import hashlib

def thing(secret):
    i = 10000
    while True:
        text = secret + str(i)

        hashed = hashlib.md5(bytes(text, 'utf-8')).hexdigest()

        if hashed[:6] == '000000':
            return text, hashed
        i +=1 

def main():
    secret = 'yzbqklnj'
    print(thing(secret))
    


if __name__ == '__main__':
    main()