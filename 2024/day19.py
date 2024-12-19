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

@functools.cache
def check(towels, pattern):
    if len(pattern) == 0:
        return 1

    possible = 0

    for towel in towels:
        if pattern.startswith(towel):
            possible += check(towels, pattern[len(towel):])

    return possible


def part1(data):
    lines = [line.rstrip() for line in data]

    towel_line, _, *patterns = lines
    towels = tuple(towel_line.split(', '))

    return sum(1 for pattern in patterns if check(towels, pattern))


def part2(data):
    lines = [line.rstrip() for line in data]

    towel_line, _, *patterns = lines
    towels = tuple(towel_line.split(', '))

    return sum(check(towels, pattern) for pattern in patterns)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
