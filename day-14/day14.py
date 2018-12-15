#!/usr/bin/env python3
#
def main():
    recipes = '37'
    with open('input', 'r') as fp:
        val = int(fp.read().strip())
    elf1 = 0
    elf2 = 1
    while str(val) not in recipes[-8:]:
        if len(recipes) % 10000 == 0:
            print("current recipes lenght: {}".format(len(recipes)))
        recipes += str(int(recipes[elf1]) + int(recipes[elf2]))
        elf1 = (1 + int(recipes[elf1]) + elf1) % len(recipes)
        elf2 = (1 + int(recipes[elf2]) + elf2) % len(recipes)

    print(recipes[int(val):int(val) + 10])
    print(len(recipes[:-7]))

if __name__ == '__main__':
    main()