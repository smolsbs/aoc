#!/usr/bin/python3

with open('input', 'r') as fp:
    data = [int(x) for x in fp.readlines()]
print(sum(data))     # part 1

twice = False
allFreq = set([0])
freq = 0 
# part 2
while not twice:
    for i in data:
        freq += i
        if freq in allFreq:
            twice = True
            print(freq)
            break
        
        allFreq.add(freq)