import os
import argparse
import datetime
import subprocess
import requests

PY_TEMPLATE = """#!/usr/bin/env python3
def main():
    with open('input', 'r') as fp:
        data = [x for x in fp.readlines()]

if __name__ == '__main__':
    main()"""

def create(args):
    os.mkdir(args['dayDir'])
    os.chdir(args['dayDir'])
    open('README.md', 'w').close()
    open('input', 'w').close()
    fn = 'day' + str(args['day']) + '.py'
    fp = open(fn, 'w')
    fp.write(PY_TEMPLATE)
    fp.close()


def fetch_input(args):
    if args['dayDir'] != os.getcwd().split('\\')[-1]:
        if args['dayDir'] not in os.listdir():
            os.mkdir(args['dayDir'])
        os.chdir(args['dayDir'])

    url = "https://adventofcode.com/2015/day/" + str(args['day']) + "/input"
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
                        help='Sets the day to x.')
    parser.add_argument('-f', '--fetch',
                        action='store',
                        default='CREATE',
                        type=str2bool,
                        dest='fetch',
                        help='Sets if input should be fetched or not')

    res = parser.parse_args()
    
    args = {'root': os.getcwd(),
            'create': res.create,
            'fetch': res.fetch,}

    if res.day is None:
        args['day'] = datetime.datetime.today().day
    else:
        args['day'] = res.day
    with open('config', 'r') as fp:
        args['cookie'] = {"session": fp.read().strip('\n')}

    args['dayDir'] = 'day-' + "{:02d}".format(int(args['day']))

    if args['create']:
        create(args)

    if args['fetch']:
        fetch_input(args)


if __name__ == '__main__':
    main()
