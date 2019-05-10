#! python

from collections import deque
from functools import reduce

class knotHash():
    def __init__(self, seq=None):
        self._list = deque([x for x in range(256)])
        self._skipSize = 0
        self._currPos = 0
        self._lenSeq = seq
        print(self._lenSeq)

    def runSeq(self, nRounds):
        if self._lenSeq == None:
                raise Exception("Please add a sequence.")
        for _ in range(nRounds):
            for i in self._lenSeq:
                self.reverseSection(i)
                self.moveCursor(i)

        self._list.rotate(self._currPos)

    def part1Out(self):
        print(self._list[0] * self._list[1])
    
    def reverseSection(self, n):
        if n == 1:
            return
        aux = list(self._list)
        aux[:n] = reversed(aux[:n])
        self._list = deque(aux)
    
    def moveCursor(self, length):
        if length > 256: 
            raise Exception("n bigger than maxlen")
        n = self._skipSize + length
        self._currPos += n
        self._list.rotate(-n)
        self._skipSize += 1

    def reset(self, seq):
        self._list = deque([x for x in range(256)])
        self._skipSize = 0
        self._currPos = 0
        self._lenSeq = seq

    def denseHash(self):
        out = ''
        sparseHash = list(self._list)
        for chunck in [sparseHash[i:i + 16] for i in range(0, len(sparseHash), 16)]:
            out += "{:02x}".format(reduce(lambda a, b: a ^ b, chunck))
        return out

def main():
    with open('input') as fp:
        a = fp.read().strip()
        dataP1 = list(map(int, a.split(',')))
        dataP2 = list(map(ord, a)) + [17, 31, 73, 47, 23]

    #part 1 (nRounds = 1, sequence is straight from input)
    algo = knotHash(dataP1)
    algo.runSeq(1)
    algo.part1Out()

    # part 2 = ascii int of every char of input, plus trailing numbers. Run 64 times and hash it
    algo.reset(dataP2)
    algo.runSeq(64)
    print(algo.denseHash())

if __name__ == '__main__':
    main()