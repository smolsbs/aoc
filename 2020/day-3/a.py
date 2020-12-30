import math


def main(*values):

    with open ('input','r') as f:
        datalist = f.read().splitlines()

    pathList = list()

    for x in datalist:
        pathList.append(list(x))
    
    slopeValues = list()

    for slopes in values:
        y = slopes[1]
        j = 0
        z = 0

        for i in range(y, len(pathList), y):
            j += slopes[0]
            
            if j > len(pathList[0])-1:
                j-=len(pathList[0])

            if pathList[i][j] == '#':
                b = pathList[i]
                b[j] = 'X'
                z = z + 1
            print(''.join(b))
            #print('px:{:2d} py:{:3d} trees:{}'.format(j, i, z) )

        print("number of trees are : {}".format(z))            
        slopeValues.append(z)


    results = math.prod(slopeValues)
    print ("multplying trees = {}".format(results))


if __name__ == '__main__':
    main((3,1))
