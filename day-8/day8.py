#!/usr/bin/env python3

# (2 3 {0 3 10 11 12} {1 1 [0 1 99] 2} 1 1 2)
# Specifically, a node consists of:

# A header, which is always exactly two numbers:
# - The quantity of child nodes.
# - The quantity of metadata entries.
# - Zero or more child nodes (as specified in the header).
# - One or more metadata entries (as specified in the header).

def main():
    # with open('sinput', 'r') as fp:
    #     data = [int(x) for x in fp.read().split(' ')]
    data = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    max_len = len(data)
    a = {'index': 0,
        'metadata': 0}
    while (a['index'] < len(data)):
        a = node(data, a)

    print(args['metadata'])
        
def node(data, args):
    print(data)
    n_childs = args['index']
    n_meta = args['index'] + 1
    args['index'] += 2
    if n_childs > 0:
        for child in range(n_childs):
            args = node(data, args)
    elif n_childs == 0:
        for _ in range(n_meta):
            args['metadata'] += data[args['index']]
            args['index'] += 1
    return args





if __name__ == '__main__':
    main()