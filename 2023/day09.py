import fileinput
import re
import itertools
import math
import functools
import collections


def parse_input(data):
    for line in data:
        yield [int(item) for item in line.split(' ')]


def solve(seq):
    if all(map(lambda item: item == 0, seq)):
        return [0]

    else:
        differences = solve([b - a for a, b in itertools.pairwise(seq)])

        # return [seq[0] - v[0]] + seq[:] + [seq[-1] + v[-1]]
        return [seq[0] - differences[0], seq[-1] + differences[-1]]


def part1(data):
    return sum(solve(sequence)[-1] for sequence in parse_input(data))


def part2(data):
    return sum(solve(sequence)[0] for sequence in parse_input(data))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
