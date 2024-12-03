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
    # lines = [''.join(data)]
    lines = [line for line in data]
    count = 0

    for line in lines:
        # skips = re.findall('don\'t\(\)', line)

        # print('dont', len(skips))

        # skips = re.findall('do\(\)', line)

        # print('do', len(skips))

        skips = re.findall('don\'t\(\).*?do\(\)', line)

        print('sets', len(skips))

        line = re.sub(r'don\'t\(\).*?do\(\)', '', line)

        skips = re.findall('don\'t\(\).*?do\(\)', line)

        print('afte', len(skips))

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
