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


def parse_instruction(line):
    ints = extract_ints(line)
    opcode, direction, *_ = line.split(' ')

    return opcode, direction, ints


def print_grid(grid, width, height):
    for y in range(height):
        print(''.join('#' if grid.get((x, y), False) else ' ' for x in range(width)))


def part1(data):
    instructions = [parse_instruction(line) for line in data]

    width, height = 50, 6

    grid = {Point(x, y): False for x in range(width) for y in range(height)}

    for opcode, d, (a, b) in instructions:
        match opcode, d:
            case 'rect', _:
                for y in range(b):
                    for x in range(a):
                        grid[Point(x, y)] = True
            case 'rotate', 'column':
                column = collections.deque(grid[Point(a, y)] for y in range(height))
                column.rotate(b)

                for y in range(height):
                    grid[Point(a, y)] = column[y]
            case 'rotate', 'row':
                row = collections.deque(grid[Point(x, a)] for x in range(width))
                row.rotate(b)

                for x in range(width):
                    grid[Point(x, a)] = row[x]
            case _:
                raise ValueError(f'Unknown opcode: {opcode}')

    print_grid(grid, width, height)

    return sum(value for value in grid.values())


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
