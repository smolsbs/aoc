#!/usr/bin/python

from re import findall, match

def parse(room):
    codes = findall(r'(.*?)-\d', room)[0].split('-')
    sID = findall(r'\d+', room)[0]
    cSum = findall(r'\[(\w+)\]', room)[0]
    
    return codes + [sID, cSum]

def main():
    with open('input', 'r') as fp:
        for line in fp.read().strip().split('\n'):
            print(parse(line))

if __name__ == '__main__':
    main()