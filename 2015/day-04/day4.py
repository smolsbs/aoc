#!/usr/bin/env python3
#
from hashlib import md5


def run(secret: str) -> tuple:
    
    p1, p2 = (None, None)
    i = 0
    while (not p1) or (not p2):
        hashed = md5( bytes(f"{secret}{i}", 'utf-8')).hexdigest()
        if not p1 and hashed[:5] == '00000':
            p1 = i
        if not p2 and hashed[:6] == '000000':
            p2 = i
        i += 1
    
    return (p1, p2)
    

def main():
    with open('input', encoding='utf-8') as fp:
        secret = fp.read().strip()
    p1, p2 = run(secret)

    print(f"Part 1: {p1}\nPart 2: {p2}")
    


if __name__ == '__main__':
    main()