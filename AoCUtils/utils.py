from re import findall


def loadInput(inputFile, returnType=str):
    '''load and parses an aoc input file
    :param inputFile: filename for the input file
    :param returnType: type for the data to be returned. Default: str'''

    fp = open(inputFile, 'r')
    data = list(map(returnType, fp.read().strip().split('\n')))
    fp.close()

    return data

def getInts(inputFile):
    '''load and parses an aoc input file into a list of ints
    :param inputFile: filename for the input file'''
    with open(inputFile, 'r') as fp:
        data = []
        for line in fp.read().strip().split('\n'):
            data.append( findall(r'-?\d+', line) )
    return data