import os
import argparse
import datetime
import subprocess
import requests

PY_TEMPLATE = """#!/usr/bin/env python3

with open('../input', 'r') as fp:
    data = [x for x in fp.readlines()]"""


def create_dir(args):
    os.mkdir(args['dayDir'])
    os.chdir(args['dayDir'])
    os.mkdir("python")
    os.mkdir("csharp")
    print("Directories created.")


def create_files(args):
    print(os.getcwd())
    open('README.md', 'w').close()
    open('input', 'w').close()

    os.chdir('python')
    fn = 'day' + str(args['day']) + '.py'
    fp = open(fn, 'w')
    fp.write(PY_TEMPLATE)
    fp.close()
    print("Python folder populated. Switching to C#")

    os.chdir(os.path.join(args['root'], args['dayDir']))
    os.chdir('csharp')

    subprocess.run("dotnet new console", shell=False, check=True)
    print("C# folder populated.\n Code away")


def fetch_input(args):
    os.chdir(args['root'])
    with open('config', 'r') as fp:
        cookie = {"session": fp.read().strip('\n')}
    if args['dayDir'] not in os.listdir():
        os.mkdir(args['dayDir'])
    os.chdir(args['dayDir'])

    url = "https://adventofcode.com/2018/day/" + str(args['day']) + "/input"
    headers = {"user-agent": 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"}
    req = requests.get(url, stream=True, headers=headers, cookies=cookie)
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
            'fetch': res.fetch}
    if res.day is None:
        args['day'] = datetime.datetime.today().day
    else:
        args['day'] = res.day

    args['dayDir'] = 'day-' + str(args['day'])

    if args['create'] and not args['fetch']:
        create_dir(args)
        create_files(args)
    elif res.create and args['fetch']:
        create_dir(args)
        create_files(args)
        fetch_input(args)
    elif not args['create'] and args['fetch']:
        fetch_input(args)


if __name__ == '__main__':
    main()
