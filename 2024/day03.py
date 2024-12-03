import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def extract_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))


def total_instructions(line):
    matches = re.findall(r'mul\(\d+,\d+\)', line)

    total = sum(math.prod(extract_ints(match)) for match in matches)

    return total


def part1(data):
    single_line = ''.join(line.rstrip() for line in data)

    return total_instructions(single_line)


def part2(data):
    single_line = ''.join(line.rstrip() for line in data)

    enabled_instructions = re.sub(r'don\'t\(\).*?do\(\)', '', single_line)

    return total_instructions(enabled_instructions)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
