import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def parse_levels(data):
    for line in data:
        yield [int(item) for item in line.strip().split()]


def check_report(levels):
    '''Check that report is decreasing or increasing slowly'''
    diffs = [b - a for a, b in (zip(levels[:-1], levels[1:]))]


    all_neg = all(diff < 0 for diff in diffs)
    all_pos = all(diff > 0 for diff in diffs)

    all_small = all(abs(diff) in (1, 2, 3) for diff in diffs)

    return all_small and (all_neg or all_pos)


def generate_subreports(levels):
    '''Yield a list of reports where exactly one item was skipped'''
    for i, _ in enumerate(levels):
        yield levels[:i] + levels[i+1:]


def check_report_damper(levels):
    '''Check report with dampers

    Allow for one level to not match
    '''
    if check_report(levels):
        return True
    for sublevels in generate_subreports(levels):
        if check_report(sublevels):
            return True
    return False


def part1(data):
    return sum(check_report(levels) for levels in parse_levels(data))


def part2(data):
    return sum(check_report_damper(levels) for levels in parse_levels(data))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
