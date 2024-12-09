import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from typing import Dict


def print_disc(disc, index):
    for i in range(index):
        if i in disc:
            print(disc[i], end='')
        else:
            print('.', end='')

    print('')


def parse_disc(data):
    sizes = map(int, [line for line in data][0].strip())

    index = 0
    file_no = 0
    disc = {}
    files = {}
    spaces = {}

    for size, is_file in zip(sizes, itertools.cycle([True, False])):
        if is_file:
            files[file_no] = (index, size)

            for location in range(index, index + size):
                disc[location] = file_no
            file_no += 1
        else:
            spaces[index] = size

        index += size

    return disc, index, files, spaces



def calc_disc_checksum(disc: Dict[int, int]) -> int:
    return sum(map(math.prod, disc.items()))


def part1(data):
    disc, disc_size, _, _ = parse_disc(data)

    left = 0
    right = disc_size

    while right not in disc:
        right -= 1

    while left < right:
        while left in disc:
            left += 1

        if left >= right:
            break

        disc[left] = disc[right]
        del disc[right]

        right -= 1

        while right not in disc:
            right -= 1

    return calc_disc_checksum(disc)


def part2(data):
    disc, _, files, spaces = parse_disc(data)

    for file_no, details in reversed(files.items()):
        location, size = details

        for new_spot in range(location):
            empty_size = spaces.get(new_spot, 0)
            if empty_size >= size:
                del spaces[new_spot]
                if empty_size > size:
                    spaces[new_spot+size] = empty_size - size
                for new_location in range(new_spot, new_spot+size):
                    disc[new_location] = file_no
                for old_location in range(location, location+size):
                    del disc[old_location]

                break

    return calc_disc_checksum(disc)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
