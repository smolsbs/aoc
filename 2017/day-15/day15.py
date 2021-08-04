#! python

from re import findall

G1_FACTOR = 16807
G2_FACTOR = 48271
DIV = 2147483647

def generate(prev, factor):
    return (prev*factor) % DIV

def low12bit(n):
    return "{:032b}".format(n)[-16:]

def run(g1seed, g2seed, runs):
    matches = 0
    for _ in range(runs-1):
        if _ == 0:
            g1 = generate(g1seed, G1_FACTOR)
            g2 = generate(g2seed, G2_FACTOR)
        else:
            g1 = generate(g1, G1_FACTOR)
            g2 = generate(g2, G2_FACTOR)
        if low12bit(g1) == low12bit(g2):
            matches += 1
    

def main():
    with open('input') as fp:
        g1Seed, g2Seed = findall(r'\d+', fp.read())
    print(g1Seed, g2Seed)




if __name__ == '__main__':
    main()