#! python

def main():
    with open('input') as fp:
        data = fp.read().strip()
    p1 = 0
    p2 = 0
    max_len = len(data)
    for i in range(max_len):
        # part 1
        if data[i] == data[(i+1) % max_len ]:
            p1 += int(data[i])
        # part 2
        if data[i] == data[(max_len // 2 + i) % max_len ]:
            p2 += int(data[i])


    print(p1)
    print(p2)
if __name__ == '__main__':
    main()