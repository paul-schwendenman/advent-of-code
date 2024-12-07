import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from collections.abc import Iterable


def extract_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))


def get_possible_values(parts, acc):
    if len(parts) == 0:
        return (acc, )

    [first, *rest] = parts

    mult = get_possible_values(rest, acc * first)
    addi = get_possible_values(rest, acc + first)

    return (mult, addi)


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


def is_possible(goal, parts):
    [first, *rest] = parts
    print(list(flatten(get_possible_values(rest, first))))
    return goal in flatten(get_possible_values(rest, first))


def part1(data):
    equations = []
    for line in data:
        [goal, *parts] = extract_ints(line)
        equations.append((goal, collections.deque(parts)))

    acc = 0
    print(equations)

    for equation in equations:
        if is_possible(*equation):
            acc += equation[0]

    pass
    return acc


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
