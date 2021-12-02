#!/usr/bin/env python3

import aocUtils

def main():
    vals = {'forward': 0, 'up': 0, 'down': 0, 'aim': 0, 'depth2': 0}
    for val in aocUtils.loadInput('input'):
        k,v = val.split(' ')
        v = int(v)
        vals[k] += v
        # part 2
        if k == 'up':
            vals['aim'] -= v
        elif k == 'down':
            vals['aim'] += v
        elif k == 'forward':
            vals['depth2'] += (v * vals['aim'])
    
    p1 = vals['forward'] * (vals['down']- vals['up'])
    p2 = vals['forward'] * vals['depth2']
    print(p1)
    print(p2)

if __name__ == '__main__':
    main()