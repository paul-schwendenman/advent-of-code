import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def total_instructions(line):
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    total = 0

    for match in matches:
        nums = list(map(int, re.findall(r'\d+', match)))

        total += math.prod(nums)

    return total


def part1(data):
    lines = [line for line in data]

    return sum(total_instructions(line) for line in lines)


def part2(data):
    single_line = ''.join(line.rstrip() for line in data)

    enabled_instructions = re.sub(r'don\'t\(\).*?do\(\)', '', single_line)

    return total_instructions(enabled_instructions)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
