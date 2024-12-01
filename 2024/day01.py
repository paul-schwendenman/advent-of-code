import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def part1(data):
    lines = [line.split() for line in data]

    first = [int(one[0]) for one in lines]
    second = [int(one[1]) for one in lines]

    third = sorted(first)
    fourth = sorted(second)

    count = 0

    for n, item in enumerate(third):
        count += abs(item - fourth[n])

    return count

    print(lines)

    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
