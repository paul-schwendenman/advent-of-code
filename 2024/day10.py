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

    def __sub__(self, other):
        return Point(self.x - other[0], self.y - other[1])

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

class Offset(enum.Enum):
    TOP_LEFT = (-1, -1)
    UP = (-1, 0)
    TOP_CENTER = (-1, 0)
    TOP_RIGHT = (-1, 1)
    LEFT = (0, -1)
    CENTER_LEFT = (0, -1)
    CENTER_CENTER = (0, 0)
    RIGHT = (0, 1)
    CENTER_RIGHT = (0, 1)
    BOTTOM_LEFT = (1, -1)
    DOWN = (1, 0)
    BOTTOM_CENTER = (1, 0)
    BOTTOM_RIGHT = (1, 1)

    def __mul__(self, scalar):
        if isinstance(scalar, int):
            return (self.value[0] * scalar, self.value[1] * scalar)
        elif isinstance(scalar, tuple):
            return (self.value[0] * scalar[0], self.value[1], scalar[1])

    def __getitem__(self, index):
        return self.value[index]

    def __eq__(self, tuple):
        return len(tuple) == 2 and self.value[0] == tuple[0] and self.value[1] == tuple[1]

    def rotate(self, clockwise=True):
        x, y = self.value

        return Offset(y, -x) if clockwise else Offset(-y, x)

    @classmethod
    def cardinal(cls):
        return (cls.UP, cls.LEFT, cls.RIGHT, cls.DOWN)

    @classmethod
    def diagonal(cls):
        return (cls.TOP_LEFT, cls.TOP_RIGHT, cls.BOTTOM_LEFT, cls.BOTTOM_RIGHT)

    @classmethod
    def all(cls):
        return cls.cardinal() + cls.diagonal()


def parse_grid(data, *, exclude=''):
    grid = {}
    markers = collections.defaultdict(list)

    for j, line in enumerate(data):
        for i, char in enumerate(line.rstrip()):
            here = Point(i, j)

            grid[here] = char

            if char not in exclude:
                markers[char].append(here)

    return grid, i, j, markers


def grid_search(start, grid, check_goal, get_next, track_paths=True, strategy='bfs'):
    queue = collections.deque([(start,)])

    if strategy == 'bfs':
        pop_item = queue.popleft
    else:
        pop_item = queue.pop

    found = set()

    while queue:
        path = pop_item()
        location = path[-1]
        current = path if track_paths else location

        if location not in grid:
            continue

        if current in found:
            continue

        if check_goal(location, grid):
            found.add(current)
            continue

        for neighbor in get_next(location, grid):
            next_item = path + (neighbor,)
            queue.append(next_item)

    return len(found)


def part1(data):
    grid, _, _, markers = parse_grid(data)

    # return sum(search(trailhead, grid, '9') for trailhead in markers['0'])
    def check_goal(location, grid):
        return grid[location] == '9'

    def get_next(location, grid):
        for next_location in [location + dir for dir in Offset.cardinal()]:
            if next_location not in grid:
                continue
            if grid.get(next_location, '') == str(int(grid[location]) + 1):
                yield next_location

    return sum(grid_search(trailhead, grid, check_goal, get_next, track_paths=False) for trailhead in markers['0'])


def part2(data):
    grid, _, _, markers = parse_grid(data)

    def check_goal(location, grid):
        return grid[location] == '9'

    def get_next(location, grid):
        for next_location in [location + dir for dir in Offset.cardinal()]:
            if next_location not in grid:
                continue
            if grid.get(next_location, '') == str(int(grid[location]) + 1):
                yield next_location

    return sum(grid_search(trailhead, grid, check_goal, get_next, 'dfs') for trailhead in markers['0'])


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
