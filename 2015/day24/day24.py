import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import operator
import typing
from functools import reduce
from operator import mul


def part1(data, number_of_groups=3):
    weights = [int(line) for line in data]

    goal_weight = sum(weights) // number_of_groups

    for group_size in range(len(weights)):
        for group in itertools.combinations(weights, group_size):
            if sum(group) == goal_weight:
                return reduce(mul, group)


def part2(data):
    return part1(data, 4)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
