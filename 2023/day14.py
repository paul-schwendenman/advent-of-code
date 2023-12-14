import fileinput
import re
import itertools
import math
import functools
import collections
import enum
from tqdm import tqdm

class Direction(tuple, enum.Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)


class Point(collections.namedtuple('Point', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])


def transpose(grid):
    return list(zip(*grid))

def parse_data(data):
    grid = {}

    for j, line in enumerate(data):
        for i, space in enumerate(line.strip()):
            grid[Point(i, j)] = space
    else:
        max_x, max_y = i + 1, j + 1

    return grid, (max_x, max_y)


def freeze_data(grid, max_x, max_y):
    for y in range(0, max_y):
        for x in range(0, max_x):
            pass


def tilt(grid, max_x, max_y, shift=Direction.NORTH):
    moved = True
    while moved:
        moved = False

        for j in range(0, max_y):
            for i in range(0, max_x):
                pos = Point(i, j)
                next_pos = pos + shift

                if grid[pos] in ('.', '#') or next_pos not in grid:
                    continue
                if grid[next_pos] == '.':
                    moved = True
                    grid[next_pos] = 'O'
                    grid[pos] = '.'
    return grid


def cycle_tilts(grid, max_x, max_y):
    north = tilt(grid, max_x, max_y, Direction.NORTH)
    west = tilt(north, max_x, max_y, Direction.WEST)
    south = tilt(west, max_x, max_y, Direction.SOUTH)
    east = tilt(south, max_x, max_y, Direction.EAST)

    return east


def score_grid(grid, max_y):
    return sum(max_y - y for (_, y), space in grid.items() if space == 'O' )


def part1(data):
    grid, (max_x, max_y) = parse_data(data)

    grid = tilt(grid, max_x, max_y)

    return score_grid(grid, max_y)


def part2(data, goal=1_000_000_000):
    grid, (max_x, max_y) = parse_data(data)
    grids = {}

    for index in itertools.count(1):
        grid = (cycle_tilts(grid, max_x, max_y))

        key = hash(tuple(grid.items()))

        if key in grids:
            cycle_length = index - grids[key][0]

            for cycle, score in grids.values():
                if cycle >= grids[key][0] and cycle % cycle_length == goal % cycle_length:
                    return score

        grids[key] = (index, score_grid(grid, max_y))


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
