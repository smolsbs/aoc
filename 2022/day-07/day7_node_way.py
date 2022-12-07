#! /usr/bin/env python3

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.childs = []
        self.files = []

    def get_size(self):
        _s = 0
        for child in self.childs:
            _s += child.get_size()
        _s += sum([f[1] for f in self.files])
        
        return _s


def get_sizes(root_node):
    _s = [(root_node.name, root_node.get_size())]
    
    if len(root_node.childs) == 0:
        return _s

    for child in root_node.childs:
        _s += get_sizes(child)

    return _s

def solve(root_node):
    thing = get_sizes(root_node)
    aval_space = 70000000 - thing[0][1]
    p1 = 0
    p2 = None

    thing = sorted(thing, key= lambda x: len(x[0].split('/')), reverse=True)

    for v in thing:
        
        if (not p2) and (v[1] + aval_space >=  30000000):
            p2 = v[1]

        if v[1] <= 100000:
            p1 += v[1]
    
    return p1, p2

def parse(data):
    root = Node('root')
    cNode = root
    for l in data[1:]:
        if l.startswith('$'):
            aux = l[2:].split(' ')
        else: 
            aux = l.split(' ')

        if aux[0] == 'cd':
            if aux[1] != '..':
                newNode = Node(f"{cNode.name}/{aux[1]}", cNode)
                cNode.childs.append(newNode)
                cNode = newNode
            else:
                cNode = cNode.parent
            
        elif aux[0] not in {'ls', 'dir'}:
            fn, size = aux[1], int(aux[0])
            cNode.files.append((fn, size))

    return root

def loadInput(path):
    with open(path, 'r') as fp:
        data = fp.read().strip().split('\n')
    
    return data

def run(path):
    data = loadInput(f"{path}/input")
    tree = parse(data)

    return solve(tree)
