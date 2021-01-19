#!/usr/bin/env python3
def part1(data):
    one, three = (0,0) 
    for i in range(len(data)-1):
        dif = data[i+1] - data[i]
        if dif == 1:
            one += 1
        elif dif == 3:
            three += 1
        
    print("part 1: %d" % (one*three))

def part2(d):
    graph = {0:1}
    # https://dev.to/sleeplessbyte/comment/194fe
    for i in range(1, len(d)):
        asdf = d[max(0,i-3):i]
        graph[d[i]] = sum( [graph[v] for v in asdf if abs(d[i] - v) <= 3]  )
    print("part 2: %d" % graph[d[-1]])

def main():
    with open('input', 'r') as fp:
        data = [0] + sorted([int(x) for x in fp.readlines()])
    data.append(data[-1] + 3)

    part1(data)
    part2(data)


if __name__ == '__main__':
    main()