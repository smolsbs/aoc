import re
import numpy as np


def main():
    with open('../input', 'r') as fp:
        data = [read_coords(x) for x in fp.readlines()]
    n = 1000 # dimention of 2D array

    # each cell on this 2D array is a list so we can append each claim ID and check afterwards
    fabric = [[[] for i in range(n)] for j in range(n)]
    for claim in data:
        # create size boundaries to add to fabric array
        lc = claim['coords'][0]
        rc = lc + claim['size'][0]
        ur = claim['coords'][1]
        br = ur + claim['size'][1]

        # populate fabric array with claim id, appending it to the list
        for i in range(ur, br):
            for j in range(lc, rc):
                fabric[i][j].append(claim['id'])

    # check for overlaping claims
    overlap = 0         
    for i in range(n):
        for j in range(n):
            if len(fabric[i][j]) > 1:
                overlap += 1
    print("Overlaped inches: %d" % overlap)
    print("Unique ID: %d" % check_unique_claim(data, fabric))


def check_unique_claim(data, fabric):
    for claim in data:
        unique = True
        lc = claim['coords'][0]
        rc = lc + claim['size'][0]
        ur = claim['coords'][1]
        br = ur + claim['size'][1]
        for i in range(ur, br):
            for j in range(lc, rc):
                if len(fabric[i][j]) > 1:
                    unique = False
                    break
            if unique is False:
                break
        if unique:
            return claim['id']

# reads data line, fetches necessary data using regex,
# formats id, coordinates and size as a dict and returns it
# so it can be appended to data
def read_coords(claim):

    aux = re.match("\#(\d+) \@ (\d+),(\d+)\: (\d+)x(\d+)", claim)
    return {'id': int(aux[1]),
            'coords': (int(aux[2]), int(aux[3])),
            'size': (int(aux[4]), int(aux[5]))}


if __name__ == '__main__':
    main()
    
            
