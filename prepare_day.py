#!  /usr/bin/env python3

import argparse
import datetime
import os
import sys

import requests

ROOT_DIR = os.getcwd()

PY_TEMPLATE = """#!/usr/bin/env python3

import aocUtils

def run(path):
    data = aocUtils.loadInput(f"{path}/input")

    p1 = None
    p2 = None

    return (p1, p2)

# === Testing suite ===
def get_sinput_path():
    from pathlib import Path
    return Path(__file__).parent.absolute() 

def test_p1():
    raise NotImplementedError

def test_p2():
    raise NotImplementedError
"""

def check_if_dir_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create(args, verbose=False):
    _path = f"{ROOT_DIR}/{args['year']}/day-{args['day']:02d}"
    print(_path)
    check_if_dir_exists(_path)
    os.chdir(_path)

    open('README.md', 'w').close()
    open('input', 'w').close()
    fn = "day{}.py".format(args['day'])
    fp = open(fn, 'w')
    fp.write(PY_TEMPLATE)
    fp.close()


def fetch_input(args, verbose=False):
    _path = f"{ROOT_DIR}/{args['year']}/day-{args['day']:02d}"
    check_if_dir_exists(_path)
    os.chdir(_path)

    url = f"https://adventofcode.com/{args['year']}/day/{args['day']}/input"
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"}
    req = requests.get(url, stream=True, headers=headers, cookies=args['cookie'])
    req.raise_for_status()

    fp = open('input', 'w')
    fp.write(req.text)
    fp.close()


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--create', '-c',
                        action='store_true',
                        dest='create',
                        help='Creates a folder with the current day, or with a specific day, if -d is used')
    parser.add_argument('-d',
                        action='store',
                        dest='day',
                        type=int,
                        help='Sets the day to x.')
    parser.add_argument('-f', '--fetch',
                        action='store',
                        default='CREATE',
                        type=str2bool,
                        dest='fetch',
                        help='Sets if input should be fetched or not')
    parser.add_argument('-y', '--year',
                        action='store',
                        dest='year',
                        type=int,
                        help='Sets the year of the event. Defaults to the current year.')
    res = parser.parse_args()

    args = {'create': res.create,
            'fetch': res.fetch,
            'curAdr': os.getcwd()}

    if res.day is None:
        args['day'] = int(datetime.datetime.today().day)
    else:
        args['day'] = res.day

    if res.year is None:
        args['year'] = int(datetime.datetime.today().year)
    else:
        args['year'] = res.year

    with open('config', 'r') as fp:
        args['cookie'] = {"session": fp.read().strip('\n')}

    if args['create']:
        create(args)

    if args['fetch']:
        fetch_input(args)


if __name__ == '__main__':
    main()
