import fileinput
import re
import itertools
import math
import functools
import collections

def solve(seq):
    if all(map(lambda item: item == 0, seq)):
        return [0]

    else:
        differences = solve([b - a for a, b in itertools.pairwise(seq)])

        # return [seq[0] - v[0]] + seq[:] + [seq[-1] + v[-1]]
        return [seq[0] - differences[0], seq[-1] + differences[-1]]


def part1(data):
    acc = 0

    for line in data:
        seq = [int(item) for item in line.split(' ')]

        acc += solve(seq)[-1]

    return acc


def part2(data):
    acc = 0

    for line in data:
        seq = [int(item) for item in line.split(' ')]

        acc += solve(seq)[0]

    return acc


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
