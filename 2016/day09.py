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


def decompress(file):
    bracket = re.search(r'\((\d+)x(\d+)\)', file)

    if not bracket:
        return file

    position = bracket.start(0)
    length = int(bracket.group(1))
    repeat = int(bracket.group(2))
    start = position + len(bracket.group())
    end = start + length

    return file[:position] + file[start:end] * repeat + decompress(file[end:])


def decompress2(file):
    bracket = re.search(r'\((\d+)x(\d+)\)', file)

    if not bracket:
        return file

    position = bracket.start(0)
    length = int(bracket.group(1))
    repeat = int(bracket.group(2))
    start = position + len(bracket.group())
    end = start + length

    return file[:position] + decompress2(file[start:end]) * repeat + decompress2(file[end:])


def part1(data):
    return len(decompress(''.join(line.rstrip() for line in data)))


def part2(data):
    return len(decompress2(''.join(line.rstrip() for line in data)))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
