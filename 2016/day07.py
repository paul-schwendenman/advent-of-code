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
    matches = re.findall(r'(.?(\w)(\w)\3\2.?)', ip)

    has_abba = any(match[1] != match[2] for match in matches)
    has_hypernet_abba = not all(match[0][0] != '[' and match[0][-1] != ']' for match in matches)


    return has_abba and not has_hypernet_abba


def part1(data):
    return sum(1 for line in data if check_ip(line.rstrip()))


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
