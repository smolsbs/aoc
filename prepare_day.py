#!  /usr/bin/env python3

import argparse
import datetime
import os
import sys

import requests

PY_TEMPLATE = """#!/usr/bin/env python3

import aocUtils

def main():
    data = aocUtils.loadInput('input')

    p1 = None
    p2 = None

    print(f'part1: {p1}')
    print(f'part2: {p2}')

if __name__ == '__main__':
    main()"""

def checkIfDirExists(dir, root=None, verbose=False):
    if sys.platform == 'linux':
        delim = '/'
    else:
        delim = '\\'
    
    root = os.getcwd().split(delim)
    listDir = os.listdir()
    if dir == root[-1] or dir == root[-2] or (dir in listDir):
        return True
    else:
        os.mkdir(dir)
        return False


def create(args, verbose=False):
    
    checkIfDirExists(args['year'])
    os.chdir(args['year'])
    checkIfDirExists(args['dayDir'])
    os.chdir(args['dayDir'])

    open('README.md', 'w').close()
    open('input', 'w').close()
    fn = "day{}.py".format(args['day'])
    fp = open(fn, 'w')
    fp.write(PY_TEMPLATE)
    fp.close()


def fetch_input(args, verbose=False):
    if not checkIfDirExists(args['year']):
        os.chdir(args['year'])
    if not checkIfDirExists(args['dayDir']):
        os.chdir(args['dayDir'])
    url = "https://adventofcode.com/{:s}/day/{:s}/input".format(args['year'], args['day'])
    headers = {"user-agent": 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"}
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
                        type=str,
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
                        type=str,
                        help='Sets the year of the event. Defaults to the current year.')
    res = parser.parse_args()
    
    args = {'root': os.getcwd(),
            'create': res.create,
            'fetch': res.fetch,
            'curAdr': os.getcwd()}

    if res.day is None:
        args['day'] = str(datetime.datetime.today().day)
    else:
        args['day'] = res.day

    if res.year is None:
        args['year'] = str(datetime.datetime.today().year)
    else:
        args['year'] = res.year
    
    
    with open('config', 'r') as fp:
        args['cookie'] = {"session": fp.read().strip('\n')}

    args['dayDir'] = "day-{:02d}".format(int(args['day']))
    if args['create']:
        create(args)

    if args['fetch']:
        fetch_input(args)


if __name__ == '__main__':
    main()
