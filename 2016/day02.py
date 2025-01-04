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


keypad = {
    Point(0, 0): '1',
    Point(1, 0): '2',
    Point(2, 0): '3',
    Point(0, 1): '4',
    Point(1, 1): '5',
    Point(2, 1): '6',
    Point(0, 2): '7',
    Point(1, 2): '8',
    Point(2, 2): '9',
}


directions = {
    'U': Offset.UP,
    'D': Offset.DOWN,
    'L': Offset.LEFT,
    'R': Offset.RIGHT,
}


def part1(data):
    nums = ""
    location = Point(1,1)

    for line in data:
        for char in line.rstrip():
            next_location = location + directions[char]

            if next_location in keypad:
                location = next_location

        nums += keypad[location]

    return int(nums)


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
