from itertools import permutations

max_x = 98
max_y = 97
xx = list(range(max_x))
yy = list(range(max_y))

allpos = []
for x in xx:
    for y in yy:
        allpos.append( (x,y) )

print(len(allpos))