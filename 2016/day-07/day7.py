#!/usr/bin/python
from re import findall


def checkerTLS(word):
    for i in range(len(word)-3):
        aux = word[i:i+4]
        if aux[:2] == aux[:-3:-1]:
            if aux[0] == aux[1] == aux[2] == aux[3]:
                continue
            return True
        
    return False

def checkerSSLoutside(word):
    aba = []
    for i in range(len(word)-2):
        aux = word[i:i+3]
        if aux[0] == aux[2] and aux[0] != aux[1]:
            aba.append(aux[:2])
        
    if len(aba) != 0:
        return aba
    return False

def checkerSSLinside(word, aba):
    for i in range(len(word)-2):
        aux = word[i:i+3]
        if aux[0] == aux[2] and aux[0] != aux[1]:
            for token in aba:
                if aux[0] == token[1] and aux[1] == token[0]:
                    return True
    return False


def supportedId(addr, part2=False):
    inside = set(findall('\[\w+\]', addr))
    outside = set(findall('\w+',addr)) - inside
    
    # TLS checker
    if not part2:
        for w in inside:
            if checkerTLS(w) == True:
                return 0    # if not valid
        for w in outside:
            if checkerTLS(w) == True:
                return 1 # if valid
        return 0
    
    # SSL checker
    else:
        aba = []
        for w in outside:
            outs = checkerSSLoutside(w)
            if outs:
                for o in outs:
                    aba.append(o)
        if len(aba) == 0:
            return 0
        for w in inside:
            if checkerSSLinside(w, aba) == True:
                return 1
        return 0


def main():
    validIpTLS, validIpSSL = (0,0)
    with open('input', 'r') as fp:
        for line in fp.read().strip().split('\n'):



            validIpTLS += supportedId(line)
            validIpSSL += supportedId(line, True)

    print(validIpTLS)
    print(validIpSSL)


if __name__ == '__main__':
    main()