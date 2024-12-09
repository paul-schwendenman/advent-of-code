import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def print_disc(disc, index):
    for i in range(index):
        if i in disc:
            print(disc[i], end='')
        else:
            print('.', end='')

    print('')


def calc_disc_checksum(disc, max_size):
    acc = 0
    for i in range(max_size):
        acc += i * disc.get(i, 0)

    return acc


def part1(data):
    line = [line for line in data][0].strip()

    index = 0
    file_no = 0
    disc = {}

    for char, is_file in zip(line, itertools.cycle([True, False])):
        size = int(char)

        for _ in range(size):
            if is_file:
                disc[index] = file_no
            index += 1

        if is_file:
            file_no += 1

    left = 0
    right = index

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

    return calc_disc_checksum(disc, index)


def part2(data):
    line = [line for line in data][0].strip()

    index = 0
    file_no = 0
    disc = {}
    files = {}
    spaces = {}

    for char, is_file in zip(line, itertools.cycle([True, False])):
        size = int(char)

        if is_file:
            files[file_no] = (index, size)
        else:
            spaces[index] = size

        for _ in range(size):
            if is_file:
                disc[index] = file_no
            index += 1

        if is_file:
            file_no += 1

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

    return calc_disc_checksum(disc, index)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
