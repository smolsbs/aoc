#!/usr/bin/env python3

import aocUtils

CYCLES = {20, 60, 100, 140, 180, 220}


def is_displayed(head, pos):
    p = abs((head % 40) - pos)

    if p <= 1:
        return True
    return False

def create_display(display):
    _print = "\n"
    for i in range(6):
        _print += f"{''.join(display[40*i:40*(i+1)])}\n"

    return _print

def run_pc(data):
    cycle = 0
    idx = 0
    reg = 1
    data_len = len(data)
    wait = 0
    sig_str = 0

    display = [' ' for _ in range(40*6)]
    head = 0

    while idx <= data_len:
        # load the command and its wait time if wait is 0
        if wait == 0:
            cmd = data[idx].split(' ')
            if cmd[0] == 'noop':
                to_add = 0
                wait = 1
            elif cmd[0] == 'addx':
                to_add = int(cmd[1])
                wait = 2
        
        # during cycle things
        else:
            cycle += 1
            wait -= 1

            head = cycle - 1
            if is_displayed(head, reg):
                display[head] = '█'
            
            if cycle in CYCLES:
                sig_str += cycle * reg

        # end of cycle things  
        if wait == 0: 
            reg += to_add
            idx += 1

    return sig_str, create_display(display)

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    return run_pc(data)
