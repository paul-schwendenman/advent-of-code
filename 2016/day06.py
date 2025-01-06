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


def part1(data):
    lines = [line.rstrip() for line in data]
    columns = [col for col in zip(*lines)]

    return ''.join(collections.Counter(column).most_common(1)[0][0] for column in columns)


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
