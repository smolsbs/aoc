#!/usr/bin/env python3

def part1(data):
    _increases = 0

    curr_val = data[0]
    for v in data[1:]:
        if v > curr_val:
            _increases += 1
        curr_val = v
    
    return f'part 1: {_increases}'

def part2(data):
    _increases = 0
    curr_val = sum(data[:3])
    for i in range(1, len(data)-2):
        val = sum(data[i:i+3])
        if val > curr_val:
            _increases += 1
        curr_val = val

    return f'part 2: {_increases}'

def main():
    with open('input', 'r') as fp:
        data = [int(x) for x in fp.read().strip().split('\n')]

    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()