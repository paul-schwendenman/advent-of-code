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

def parse(data):
    lines = [line.rstrip() for line in data]

    designs = lines[2:]
    towels = tuple(lines[0].split(', '))

    return designs, towels


@functools.cache
def check(towels, design):
    if len(design) == 0:
        return 1

    return sum(check(towels, design[len(towel):]) for towel in towels if design.startswith(towel))


def part1(data):
    designs, towels = parse(data)

    return sum(1 for design in designs if check(towels, design))


def part2(data):
    designs, towels = parse(data)

    return sum(check(towels, design) for design in designs)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
