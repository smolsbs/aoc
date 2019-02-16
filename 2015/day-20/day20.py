#!/usr/bin/python

# import matplotlib.pyplot as plt


def part1(N):
    houses = [0 for _ in range(N // 10)]

    for i in range(1, N // 10):
        for j in range(i, N // 10, i):
            houses[j] += i * 10

    print("all houses ran. finding smallest number")
    for x in range(N // 10):
        if houses[x] >= N:
            print(x)
            break

def part2(N):
    houses = [0 for _ in range(N // 10)]

    for i in range(1, N // 10):
        n_houses = 0
        for j in range(i, N // 10, i):
            if n_houses < 50:
                houses[j] += i * 11
                n_houses += 1
            else:
                break

    print("all houses ran. finding smallest number")
    for x in range(N // 10):
        if houses[x] >= N:
            print(x)
            break



def main():
    with open('input', 'r') as fp:
        data = int(fp.read().strip())
    
    # part1(data)
    part2(data)

if __name__ == '__main__':
    main()