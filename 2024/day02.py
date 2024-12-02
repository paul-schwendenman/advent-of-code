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
    count = 0
    for line in data:
        safe = True
        levels = [int(item) for item in line.strip().split()]
        # print(levels)

        diffs = [b - a for a, b in (zip(levels[:-1], levels[1:]))]
        # print(diffs)

        all_neg = all(diff < 0 for diff in diffs)
        all_pos = all(diff > 0 for diff in diffs)
        all_small = all(abs(diff) in (1, 2, 3) for diff in diffs)
        # print(all_neg, all_pos, all_small)

        if all_small and (all_neg or all_pos):
            # print("pass")
            count += 1


    pass
    return count


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
