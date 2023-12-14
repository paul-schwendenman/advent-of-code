import fileinput
import re
import itertools
import math
import functools
import collections
import enum
from tqdm import tqdm


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

    return tuple(grid.items()), (max_x, max_y)
    # return grid, (max_x, max_y)


def freeze_data(grid, max_x, max_y):
    for y in range(0, max_y):
        for x in range(0, max_x):
            pass


# @functools.lru_cache(maxsize=None)
def tilt(grid, max_x, max_y, shift):
    grid = dict(grid)
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
    return tuple(grid.items())


# @functools.lru_cache(maxsize=None)
def cycle_tilts(grid, max_x, max_y):
    north = tilt(grid, max_x, max_y, (0, -1))
    west = tilt(north, max_x, max_y, (-1, 0))
    south = tilt(west, max_x, max_y, (0, 1))
    east = tilt(south, max_x, max_y, (1, 0))

    return east


def score_grid(grid, max_y):
    return sum(max_y - y for (_, y), space in dict(grid).items() if space == 'O' )


def print_grid(grid, max_x, max_y):
    if type(grid) != dict:
        grid = dict(grid)

    for y in range(max_y):
        print(''.join(grid[(x, y)] for x in range(max_x)))
    print('')


def part1(data):
    grid, (max_x, max_y) = parse_data(data)

    grid = dict(tilt(grid, max_x, max_y, (0, -1)))

    return sum(max_y - y for (_, y), space in grid.items() if space == 'O' )

    # grid = (tilt(grid, max_x, max_y, (0, -1)))

    # print_grid(grid, max_x, max_y)

    # grid = (tilt(grid, max_x, max_y, (-1, 0)))

    # print_grid(grid, max_x, max_y)

    # grid = (tilt(grid, max_x, max_y, (0, 1)))

    # print_grid(grid, max_x, max_y)

    # grid = (tilt(grid, max_x, max_y, (1, 0)))

    # print_grid(grid, max_x, max_y)




def part2(data):
    grid, (max_x, max_y) = parse_data(data)

    grids = {}
    goal = 1_000_000_000

    for index in (range(1, goal)):
        # print("this")
        grid = (cycle_tilts(grid, max_x, max_y))

        if hash(grid) in grids:
            cycle_length = index - grids[hash(grid)][0]

            for cycle, score in grids.values():
                if cycle >= grids[hash(grid)][0] and cycle % cycle_length == goal % cycle_length:
                    return score

        grids[hash(grid)] = (index, score_grid(grid, max_y))

    # return sum(max_y - y for (_, y), space in dict(grid).items() if space == 'O' )
    pass


def main():
    try:
        print(part1(fileinput.input()))
        print(part2(fileinput.input()))
    finally:
        # print(f'tilt:  {tilt.cache_info()}')
        # print(f'cycle: {cycle_tilts.cache_info()}')
        pass


if __name__ == '__main__':
    main()
