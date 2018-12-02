import os
import argparse
import datetime
import subprocess
import requests

PY_TEMPLATE = """import sys

with open('../input', 'r') as fp:
    data = [x for x in fp.readlines()]"""


def createDir(args):
    if args.day == None:
        day = datetime.date.today().day
    else:
        day = args.day
    
    dayDir = "day-" + str(day)
    root = os.path.join(os.getcwd(), dayDir)
    os.mkdir(dayDir)
    os.chdir(dayDir)
    os.mkdir("python")
    os.mkdir("csharp")
    print("Directories created... Adding necessary files.")
    createFiles(args, root, day)

def createFiles(args, root, day):
    open('README.md', 'w').close()
    open('input', 'w').close()

    os.chdir('python')
    fn = 'day' + str(day) + '.py'
    fp = open(fn, 'w')
    fp.write(PY_TEMPLATE)
    fp.close()
    print("Python folder populated. Switching to C#")

    os.chdir(root)
    os.chdir('csharp')

    proc = subprocess.run("dotnet new console", shell=False, check=True)
    print("C# folder populated.\n Code away")

    if args.boolean:
        fetchInput(root)

def fetchInput(root, day):
    os.chdir(root)
    url = "https://adventofcode.com/2018/day/" + str(day) + "/input"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
    } 
    with open('config', 'r') as fp:
        cookie = {"session": fp.read().strip('\n')}
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
        dest='boolean',
        help='Sets if input should be fetched or not')

    res = parser.parse_args()

    createDir(res)

if __name__ == '__main__':
    main()

