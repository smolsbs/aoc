#!/usr/bin/env python3

def real_str_len(string, part1=False):
    string = list(string)
    if part1:
        leng = 0
        new_string = r''
        while string:
            c = string.pop(0)
            if c == '\\':
                c = string.pop(0)
                if c == 'x':
                    string = string[2:]
            leng += 1
        return leng
    else:
        
        while string:
            c = string.pop(0)
            if c == '\\':
                new_string += "\\\\"
            elif c == '\"':
                new_string += "\\\""
            else:
                new_string += c

        return len(new_string)
    return (leng, len(new_string))


def main():
    p1 = p2 = 0
    with open('input', 'r') as fp:
        for line in fp.read().split('\n'):
            p1 += (len(line) - real_str_len(line[1:-1], True))
            p2 += (real_str_len(line) + 6 - len(line))
    print(p1)
    print(p2)

if __name__ == '__main__':
    main()