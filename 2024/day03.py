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
        matches = re.findall(r'mul\(\d+,\d+\)', line)

        for match in matches:
            nums = list(map(int, re.findall(r'\d+', match)))

            count += math.prod(nums)

    return count


def part2(data):
    lines = [''.join(data)]
    count = 0

    for line in lines:
        subs = 1
        while subs > 0:
            line, subs = re.subn(r'don\'t\(\).*?do\(\)', '', line)
            print(subs)

        matches = re.findall(r'mul\(\d+,\d+\)', line)

        for match in matches:
            nums = list(map(int, re.findall(r'\d+', match)))

            count += math.prod(nums)

    return count


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
