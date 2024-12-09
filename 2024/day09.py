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


def part1(data):
    line = [line for line in data][0].strip()

    index = 0
    file_no = 0
    disc = {}

    for char, is_file in zip(line, itertools.cycle([True, False])):
        # print(f'{char} {is_file}')
        size = int(char)

        for _ in range(size):
            if is_file:
                disc[index] = file_no
            index += 1

        if is_file:
            file_no += 1

    # print_disc(disc, index)

    left = 0
    right = index

    while right not in disc:
        right -= 1

    # print(f's: {left} e: {right}')

    while left < right:
        while left in disc:
            left += 1

        if left >= right:
            break

        # print(f'l{left}: {disc.get(left, None)}')

        disc[left] = disc[right]
        del disc[right]
        # print_disc(disc, index)

        right -= 1

        while right not in disc:
            right -= 1

        # print(f'r{right}: {disc.get(right, None)} -> {left}')

    # print_disc(disc, index)

    acc = 0
    for i in range(index):
        acc += i * disc.get(i, 0)


    return acc

    return





    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
