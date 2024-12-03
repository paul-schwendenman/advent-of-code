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
    count = 0

    for line in lines:
        print(line)

        # matches = re.findall(r'mul\((\d+\))', line)
        matches = re.findall(r'mul\(\d+,\d+\)', line)
        print(matches)

        for match in matches:
            nums = list(map(int, re.findall(r'\d+', match)))
            print(match, math.prod(nums))
            count += math.prod(nums)

    return count


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
