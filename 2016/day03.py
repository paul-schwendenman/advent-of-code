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


def get_vertical_triangles(lines):
    for l1, l2, l3 in batched(lines, 3):
        yield l1[0], l2[0], l3[0]
        yield l1[1], l2[1], l3[1]
        yield l1[2], l2[2], l3[2]
    pass


def part1(data):
    triangles = [extract_ints(line) for line in data]

    return sum(1 for triangle in triangles if check_triangle(triangle))


def part2(data):
    lines = [extract_ints(line) for line in data]

    triangles = get_vertical_triangles(lines)

    return sum(1 for triangle in triangles if check_triangle(triangle))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
