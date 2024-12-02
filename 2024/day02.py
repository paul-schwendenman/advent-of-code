import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def check_report(levels):
    diffs = [b - a for a, b in (zip(levels[:-1], levels[1:]))]


    all_neg = all(diff < 0 for diff in diffs)
    all_pos = all(diff > 0 for diff in diffs)

    all_small = all(abs(diff) in (1, 2, 3) for diff in diffs)

    return all_small and (all_neg or all_pos)


def part1(data):
    count = 0
    for line in data:
        safe = True
        levels = [int(item) for item in line.strip().split()]

        if check_report(levels):
            # print("pass")
            count += 1


    pass
    return count


def part2(data):
    count = 0
    for line in data:
        levels = [int(item) for item in line.strip().split()]

        if check_report(levels):
            count += 1
        else:
            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i+1:]
                if check_report(new_levels):
                    count += 1
                    break

    return count


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
