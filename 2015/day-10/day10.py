#! python

def look_say(inp):
    if type(inp) != str:
        inp = str(inp)
    new_inp = []
    ch = inp[0]
    l = 1
    for i in range(1, len(inp)):
        if inp[i] == ch:
            l += 1
        if i != ch:
            new_inp += (str(l) + inp[i])
            l = 1
        if i == len(inp):
            new_inp += (str(l) + inp[i])
    return ''.join(new_inp)


def main():
    inp = str(1113122113)
    for _ in range(40):
        print("i: {}\t len:{}".format(_, len(inp)))
        inp = look_say(inp)
    print(len(inp))

if __name__ == '__main__':
    # print(look_say('1211'))
    main()
