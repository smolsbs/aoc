#!/usr/bin/env python3

from collections import defaultdict


def solve_p1(data):
    sizes = defaultdict(int)
    for _dir, files in data.items():
        _s = sum([f[1] for f in files])
        sizes[_dir] += _s
        aux = _dir
        while True:
            a = aux.split('/')
            if len(a) == 1:
                break
            a.pop()
            aux = '/'.join(a)
            sizes[aux] += _s


    return sum([v for v in sizes.values() if v <= 100000]), sizes

def solve_p2(data):
    aval_space = 70000000 - data['root']
    # 30000000
    dirs = []
    for k in data.keys():
        dirs.append((k, len(k.split('/'))) )

    dirs = sorted(dirs, key=lambda x: x[1], reverse=True)

    for d in dirs:
        if aval_space + data[d[0]] >= 30000000:
            return data[d[0]]

def parse(path):
    with open(path, 'r') as fp:
        data = fp.read().strip().split('\n')

    dirs = defaultdict(list)
    list_of_dirs = ['root']
    cDir = 'root'
    for line in data[1:]:
        if line.startswith('$'):
            a = line[2:].split(' ')
        else:
            a = line.split(' ')

        if a[0] == 'cd':
            if a[1] == '..':
                list_of_dirs.pop()
            else:
                list_of_dirs.append(a[1])
            cDir = '/'.join(list_of_dirs)

        elif a[0] not in ('ls', 'dir'):
            dirs[cDir].append( (a[1], int(a[0])) )

    return dirs

def run(path):
    data = parse(f"{path}/input")

    p1, sizes = solve_p1(data)
    p2 = solve_p2(sizes)

    return (p1, p2)
