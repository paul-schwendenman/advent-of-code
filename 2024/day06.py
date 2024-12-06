import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


class Point(collections.namedtuple('Point', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


class Direction(tuple, enum.Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def rotate(self, clockwise=False):
        x, y = self
        return Direction(y, -x) if clockwise else Direction(-y, x)


def parse_grid(data):
    grid = {}

    for j, line in enumerate(data):
        for i, char in enumerate(line.rstrip()):
            here = Point(i, j)

            grid[here] = char

            if char == '^':
                loc = Point(i, j)

    return grid, i, j, loc

def print_grid(grid, i, j, been):
    for y in range(j):
        for x in range(i):
            if (x, y) in been:
                print('^', end="")
            else:
                print(grid[(x, y)], end="")

        print()

    print()


def part1(data):
    grid, i, j, location = parse_grid(data)

    direction = Direction.UP
    been = list()
    been.append(location)

    while location in grid:
        # print_grid(grid, i, j, been)
        next_location = location + direction

        if grid.get(next_location) == '#':
            # print(f'rotating: {location} {next_location} {direction}')
            direction = direction.rotate()
        else:
            location = next_location
            been.append(next_location)

        # print(been)

    past = set(been)

    return len(past) - 1


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
