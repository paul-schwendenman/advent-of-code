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

'''
1 2 3
4 5 6
7 8 9
'''
keypad_1 = {
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

'''
    1
  2 3 4
5 6 7 8 9
  A B C
    D
'''
keypad_2 = {
    Point(0, -2): '1',
    Point(-1, -1): '2',
    Point(0, -1): '3',
    Point(1, -1): '4',
    Point(-2, 0): '5',
    Point(-1, 0): '6',
    Point(0, 0): '7',
    Point(1, 0): '8',
    Point(2, 0): '9',
    Point(-1, 1): 'A',
    Point(0, 1): 'B',
    Point(1, 1): 'C',
    Point(0, 2): 'D',
}


directions = {
    'U': Offset.UP,
    'D': Offset.DOWN,
    'L': Offset.LEFT,
    'R': Offset.RIGHT,
}


def solve(data, keypad, location):
    nums = ""

    for line in data:
        for char in line.rstrip():
            next_location = location + directions[char]

            if next_location in keypad:
                location = next_location

        nums += keypad[location]

    return (nums)


def part1(data):
    return solve(data, keypad_1, Point(1, 1))


def part2(data):
    return solve(data, keypad_2, Point(-2, 0))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
