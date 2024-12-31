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
    weights = [int(line) for line in data]

    goal_weight = sum(weights) // 3

    for group_size in range(len(weights)):
        for group in itertools.combinations(weights, group_size):
            if sum(group) == goal_weight:
                return functools.reduce(lambda a, b: math.prod([a, b]), group)





    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
