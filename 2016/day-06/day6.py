#!/usr/bin/python
from collections import Counter


def countChars(words, part2=False):
    wordsLen = len(words[0])
    counters = [Counter() for _ in range(wordsLen)]
    for word in words:
        for i in range(wordsLen):
            counters[i].update(word[i])

    w = ''
    if part2:
        for c in counters:
            w+= c.most_common()[-1][0]
    else:
        for c in counters:
            w+= c.most_common(1)[0][0]

    return w


def main():


    with open('input', 'r') as fp:
        words = [word for word in fp.read().strip().split('\n')]

    print("Part 1: {}".format(countChars(words)))
    print("Part 2: {}".format(countChars(words, True)))

if __name__ == '__main__':
    main()