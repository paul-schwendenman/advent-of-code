import fileinput
import re
import itertools
import math
import functools
import collections
import enum


def transpose(grid):
    return list(zip(*grid))


def extract_patterns(data):
    lines = ''.join(data)

    for chunk in lines.split('\n\n'):
        yield chunk.strip().split('\n')


def find_horizontal_reflection(pattern):
    for index, _ in enumerate(pattern):
        before = list(reversed(pattern[:index]))
        after = pattern[index:]

        if len(before) == 0 or len(after) == 0:
            continue

        if all(b == a for a, b in zip(before, after)):
            return index
    return 0


def count_diff(a, b):
    acc = 0
    for aa, bb in zip(a, b):
        if aa != bb:
            acc += 1

    return acc

def find_smugged_horizontal_reflection(pattern):
    for index, _ in enumerate(pattern):
        before = list(reversed(pattern[:index]))
        after = pattern[index:]

        if len(before) == 0 or len(after) == 0:
            continue

        if sum(count_diff(a, b)for a, b in zip(before, after)) == 1:
            return index
    return 0


def find_vertical_reflection(pattern):
    return find_horizontal_reflection(transpose(pattern))

def find_smugged_vertical_reflection(pattern):
    return find_smugged_horizontal_reflection(transpose(pattern))


def part1(data):
    patterns = list(extract_patterns(data))

    acc = 0

    for pattern in patterns:
        if (row_index := find_horizontal_reflection(pattern)):
            acc += row_index * 100
        elif (col_index := find_vertical_reflection(pattern)):
            acc += col_index
    return acc


def part2(data):
    patterns = list(extract_patterns(data))

    acc = 0

    for pattern in patterns:
        if (row_index := find_smugged_horizontal_reflection(pattern)):
            acc += row_index * 100
        elif (col_index := find_smugged_vertical_reflection(pattern)):
            acc += col_index
    return acc


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
