import sys
import itertools
with open('input', 'r') as fp:
    data = [x.strip('\n') for x in fp.readlines()]

def part1(data):
    a, b = 0, 0
    for line in data:
        s = {}
        for ch in line:
            if ch not in s:
                s[ch] = 1
            else:
                s[ch] += 1
        if 2 in s.values(): 
            a +=1
        if 3 in s.values(): 
            b += 1
    return a*b

def part2(data):
    combs = list(itertools.combinations(data, 2))
    ssize = len(combs[0][0]) # length of any string 
    for c in combs:
        common = ""
        diff = 0
        for i in range(ssize):
            if c[0][i] == c[1][i]:
                common += c[0][i]
            else:
                diff +=1
            if diff > 1:
                break
        if diff == 1:
            return common    
        

print(part1(data))
print(part2(data))
