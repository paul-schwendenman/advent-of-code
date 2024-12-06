import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from tqdm import tqdm


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


def print_grid(grid, i, j, been, obsticle):
    for y in range(j+1):
        for x in range(i+1):
            if (x, y) in been:
                print('^', end="")
            elif (x, y) == obsticle:
                print('O', end='')
            else:
                print(grid.get((x, y)), end="")

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

def simulate_grid(grid, location, direction, obstacle):
    direction = Direction.UP
    been = list()
    been.append((location, direction))

    while location in grid:
        next_location = location + direction

        if (next_location, direction) in been:
            return been, True

        if grid.get(next_location) == '#' or next_location == obstacle:
            print(f'rotating: {location} {next_location} {direction}')
            direction = direction.rotate()
        else:
            location = next_location
            been.append((next_location, direction))

        # print(been)

    return been, False


def part2(data):
    grid, i, j, location = parse_grid(data)

    been, _ = simulate_grid(grid, location, Direction.UP, None)

    count = 0

    for obstacle, _ in been:
    # for obstacle, _ in tqdm(been):
        path, result = simulate_grid(grid, location, Direction.UP, obstacle)

        if result:
            print_grid(grid, i,j, [i[0] for i in path], obstacle)

            count +=1

    return count
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
