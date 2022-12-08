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


def print_aval_days(year=YEAR):
    root_path = os.getcwd()
    dirs = sorted(os.listdir(f"{root_path}/{year}"))
    print(f"┏ Year: {year}")
    for folder, idx in zip(dirs, range(len(dirs))):
        if folder == '__pycache__' or folder == '__init__.py':
            continue
        if idx == len(dirs)-1:
            print(f"┗━━ {folder}")
        else:
            print(f"┣━━ {folder}")

def convert_time(time):
    if time // 10**9  != 0:
        return f"{round(time / 10**9, 3)} s"
    elif time // 10**6 != 0:
        return f"{round(time / 10**6, 3)} ms"
    elif time // 10**3 != 0:
        return f"{round(time / 10**3, 3)} us"
    else:
        return f"{time} ns"


def main():
    parser = argparse.ArgumentParser()

    req = parser.add_mutually_exclusive_group()

    req.add_argument('-p', '--print', action='store_true', dest='print')
    req.add_argument('-d', action='store', type=int, dest='day')
    parser.add_argument('-y', action='store', type=int, dest='year')

    args = parser.parse_args()

    if args.year:
        year = args.year
    else:
        year = YEAR

    if args.print:
        print_aval_days(year)
        return

    if args.day > 31 or args.day < 1:
        raise NotAValidDayError(args.day)

    _path = f"{os.getcwd()}/{year}/day-{args.day:02d}"

    # check if I have more than one python file for the day
    files = [f for f in os.listdir(_path) if f.endswith('.py')]
    if len(files) > 1:
        n_files = len(files)
        while True:
            os.system('clear')
            for f, idx in zip(files, range(n_files)):
                print(f"{idx+1}) {f}")
            try:
                usrIn = int(input("Select which file to run: "))
            except ValueError:
                print("Invalid choice.")
                time.sleep(2)
                pass
            if (usrIn > 0) and (usrIn <= n_files):
                file = files[usrIn-1]
                break
            else:
                print("\nInvalid choice.")
                time.sleep(2)
    else:
        file = files[0]

    os.system('clear')

    module_path = f"{year}.day-{args.day:02d}.{file.split('.')[0]}"

    try:
        run_day = importlib.import_module(module_path)
    except ModuleNotFoundError:
        cprint(f"Day {args.day} of year {year} not found.", 'red')
        exit(1)

    cprint(f"=== Year: {year} ===", 'blue')
    cprint(f"\nDay {args.day}\n", 'blue')
    # time it and run the day
    start = time.time_ns()
    p1, p2 = run_day.run(_path)
    stop = (time.time_ns() - start)


    cprint(f'Part 1: {p1}', 'red' if p1 is None else 'green')
    cprint(f'Part 2: {p2}', 'red' if p2 is None else 'green')
    cprint(f"\nExecution time: {convert_time(stop)}", color='grey', on_color="on_white")

if __name__ == '__main__':
    main()

