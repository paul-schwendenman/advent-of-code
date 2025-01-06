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
    print(f'--- {ip} ----')
    match = re.match(r'.*(\w)(\w)\2\1', ip)

    if not match:
        print(f'skipping: {ip}')
        return False

    print(f'group: {match.groups()}')

    match2 = re.match(r'.*\[(\w)(\w)\2\1\]', ip)

    if match2:
        return False
    groups = match.group()

    if groups[0] == groups[1]:
        return False

    print(match, match2)
    return True


def part1(data):
    return sum(1 for line in data if check_ip(line.rstrip()))


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
