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


def part1(data):
    return sum(1 for line in data if check_ip(line.rstrip()))


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
