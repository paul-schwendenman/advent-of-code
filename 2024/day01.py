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
    location_pairs = [line.split() for line in data]

    list_one = sorted(int(location_pair[0]) for location_pair in location_pairs)
    list_two = sorted(int(location_pair[1]) for location_pair in location_pairs)

    count = sum(abs(one - two) for one, two in zip(list_one, list_two))

    return count


def part2(data):
    items = [line.split() for line in data]

    locations = [int(item[0]) for item in items]
    counts = collections.Counter([int(item[1]) for item in items])

    count = sum(item * counts[item] for item in locations)

    return count


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
