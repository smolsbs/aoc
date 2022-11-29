#! /usr/bin/env python

import argparse
import importlib
import os
import time
from termcolor import cprint

YEAR = 2022


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store', required=True, type=int, dest='day')

    args = parser.parse_args()
    module_path = f"{YEAR}.day-{args.day:02d}.day{args.day}"

    run_day = importlib.import_module(module_path)
    _path = f"{os.getcwd()}/{YEAR}/day-{args.day:02d}"
    start = time.time_ns()
    run_day.run(_path)
    stop = (time.time_ns() - start) / 10**3
    cprint(f"Execution time: {stop} ms", 'green')


if __name__ == '__main__':
    # run_day = importlib.import_module('2022.day-01.day1')
    #
    # run_day.run()

    main()


