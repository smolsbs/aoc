#! /usr/bin/env python

import argparse
import importlib
import os
import time
from sys import exit
from termcolor import cprint

YEAR = 2022

class NotAValidDayError(Exception):
    def __init__(self, day):
        self.day = day
        self.message = f"{self.day} is not a valid day."
    
    def __str__(self):
        return self.message


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store', required=True, type=int, dest='day')
    parser.add_argument('-y', action='store', type=int, dest='year')

    args = parser.parse_args()

    if args.day > 31 or args.day < 1:
        raise NotAValidDayError(args.day)

    if args.year:
        year = args.year
    else:
        year = YEAR

    module_path = f"{year}.day-{args.day:02d}.day{args.day}"

    try:
        run_day = importlib.import_module(module_path)
    except ModuleNotFoundError:
        cprint(f"Day {args.day} of year {year} not found.", 'red')
        exit(1)
    
    _path = f"{os.getcwd()}/{year}/day-{args.day:02d}"
    start = time.time_ns()
    p1, p2 = run_day.run(_path)
    stop = (time.time_ns() - start) / 10**6


    cprint(f'Part1: {p1}', 'red' if p1 is None else 'green')
    cprint(f'Part2: {p2}', 'red' if p2 is None else 'green')
    cprint(f"Execution time: {stop} ms", color='grey', on_color="on_white")


if __name__ == '__main__':
    main()

