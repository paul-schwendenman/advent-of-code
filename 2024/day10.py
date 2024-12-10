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


def search(start, grid, goal='9'):
    queue = collections.deque([start])

    found = set()

    while queue:
        location = queue.popleft()

        if location not in grid:
            continue

        if location in found:
            continue

        if grid[location] == goal:
            found.add(location)
            continue

        for next_location in [location + dir for dir in Offset.cardinal()]:
            if next_location not in grid:
                continue
            if grid.get(next_location, '') == str(int(grid[location]) + 1):
                queue.append(next_location)

    return len(found)

def search2(start, grid, goal='9'):
    queue = collections.deque([(start,)])

    found = set()

    while queue:
        path = queue.popleft()
        location = path[-1]
        print(f'checking {location}')

        if location not in grid:
            print(f'out of bounds {location}')
            continue

        if path in found:
            print(f'already found {location}')
            continue

        if grid[location] == goal:
            print(f'found {location}')
            found.add(path)
            continue

        for next_location in [location + dir for dir in Offset.cardinal()]:
            if next_location not in grid:
                print(f'out of bounds {next_location} <- {location}')
                continue
            if grid.get(next_location, '') == str(int(grid[location]) + 1):
                print(f'continue {location} -> {next_location}: {grid[location]}->{grid[next_location]}')
                next_path = path + (next_location,)
                queue.append(next_path)

    return len(found)

def part1(data):
    grid, _, _, markers = parse_grid(data)

    # print(markers)
    trailheads = markers['0']

    count = 0

    for trailhead in trailheads:
        print('------ new trailhead -------')
        count += search(trailhead, grid)

    return count


def part2(data):
    grid, _, _, markers = parse_grid(data)

    # print(markers)
    trailheads = markers['0']

    count = 0

    for trailhead in trailheads:
        print('------ new trailhead -------')
        count += search2(trailhead, grid)

    return count
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
