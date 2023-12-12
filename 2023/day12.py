import fileinput
import re
import itertools
import math
import functools
import collections
import enum

def parse_line(line):
    springs, sets = line.split(' ')
    # springs = springs.split('')
    sets = [int(item) for item in sets.split(',')]

    return springs, sets

def count_arrangements(springs, sets):
    pass


def score_springs(springs):
    sets = []
    count = 0

    for spring in springs:
        print(f'{spring} {count=} {sets}')
        if spring == '#':
            count += 1
        elif spring == '.':
            if count > 0:
                sets.append(count)
            count = 0
    else:
        if count > 0:
            sets.append(count)
    return sets

def part1(data):
    acc = 0

    for line in data:
        springs, sets = parse_line(line)

        acc += count_arrangements(springs, sets)
    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
