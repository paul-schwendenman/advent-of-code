import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from utils import *


def check_ip(ip):
    pattern = re.compile(r'^(?=.*(\w)(?!\1)(\w)\2\1)(?!.*\[[^]]*(\w)(?!\3)(\w)\4\3)')

    matches = re.findall(pattern, ip)

    return len(matches) > 0

def check_ssl(ip):
    hyper = re.findall(r'\[\w+\]', ip)

    for set in hyper:
        ip = ip.replace(set, '')

    chunks = [ip[i-2:i+1] for i in range(2, len(ip)) if ip[i-2] == ip[i] and ip[i] != ip[i-1]]

    print(hyper)

    print(chunks)

    for chunk in chunks:
        hcukn = chunk[1] + chunk[0] + chunk[1]

        # if chunk[0] == chunk[1]:
        #     continue

        for h in hyper:
            # print(f'{hcukn} {chunk} \t {ip}')
            if hcukn in h:
                # print(f'{hcukn} {chunk} \t {ip}')
                return True
    else:
        print(f'no matches: {ip}')

    return False



def part1(data):
    return sum(1 for line in data if check_ip(line.rstrip()))


def part2(data):
    return sum(1 for line in data if check_ssl(line.rstrip()))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
