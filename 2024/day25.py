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

def parse_key_lock(lines):
    if all(char == '#' for char in lines[0]) and all(char == '.' for char in lines[-1]):
        type = 'lock'
    elif all(char == '.' for char in lines[0]) and all(char == '#' for char in lines[-1]):
        type = 'key'
    else:
        print(f'{lines[0]} {lines[-1]}')
        print(f'{lines}')
        raise ValueError('fail')

    heights = []

    for column in zip(*lines):
        c = collections.Counter(column)

        heights.append(c['#'] - 1)

    return type, heights


def parse_data(data):
    items = [item.split('\n') for item in ''.join(data).rstrip().split('\n\n')]
    locks, keys = [], []

    for item in items:
        type, heights = parse_key_lock(item)

        if type == 'lock':
            locks.append(heights)
        else:
            keys.append(heights)

    return locks, keys



def part1(data):
    locks, keys = parse_data(data)
    print(f'{len(locks)} {len(keys)}')
    count = 0

    for lock, key in itertools.product(locks, keys):
        print(f'{lock} {key} {[lock[index] + key[index] for index in range(5)]}')
        if all(lock[index] + key[index] <= 5 for index in range(5)):
            count += 1

    return count


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
