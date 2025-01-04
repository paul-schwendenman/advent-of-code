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


def check_triangle(triangle):
    [a, b, c] = sorted(triangle)

    return a <= b <= c and a + b > c


def part1(data):
    triangles = [extract_ints(line) for line in data]

    return sum(1 for triangle in triangles if check_triangle(triangle))


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
