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
    lines = [line for line in data]
    line = lines[0]
    print(line)

    # matches = re.findall(r'mul\((\d+\))', line)
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    print(matches)

    count = 0
    for match in matches:
        print(match)
        nums = list(map(int, re.findall(r'\d+', match)))
        count += math.prod(nums)

    return count


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
