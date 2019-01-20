#!/usr/bin/env python3

import json
import re


def parser(elem):
        if type(elem) == list:
            return sum([parser(elem) for elem in elem])
        if type(elem) == int:
            return elem
        if type(elem) != dict:
            return 0
        if "red" in elem.values():
            return 0
        return parser(list(elem.values()))


def main():
    with open('input', 'r') as fp:
        data = fp.read()
        data_json = json.loads(data)

    # ns = re.findall('\-?\d+', data)
    # print(sum([int(i) for i in ns])) # part 1

    _sum = parser(data_json)
    print(_sum)
if __name__ == '__main__':
    main()