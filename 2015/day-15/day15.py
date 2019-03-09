#!/usr/bin/python
from collections import defaultdict
from re import findall

def listAllAmounts(total=100):
    amts = []
    for a in range(1, 101):
        for b in range(1, 101-a):
            for c in range(1, 101-(a+b)):
                for d in range(1, 101-(a+b+c)):
                    if a+b+c+d == total:
                        amts.append({'Frosting':a, 'Candy':b, 'Butterscotch':c,'Sugar':d})
    return amts

def getScore(ing, n):
    return sum([max(0, n*ing[i]) for i in ['c', 'd', 'f', 't']])

def main():
    ings = defaultdict(dict)
    with open('input', 'r') as fp:
        for line in fp.read().strip().split('\n'):
            ing = line.split(':')[0]
            c, d, f, t, cal = map(int, findall(r'\-?\d+', line))
            ings[ing] = {'c':c, 'd':d, 'f':f, 't':t, 'cal':cal}
    amnts = []
    amounts = listAllAmounts()
    for a in amounts:
        score = 0
        for k, v in a:
            score += getScore(ings[k], v)
        amnts.append(score)



    print(sorted(amnts, reverse=True)[0:10])




if __name__ == '__main__':
    main()
    # main(500)
