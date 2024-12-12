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

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

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


def part1(data):

    grid, _, _, markers = parse_grid(data)
    acc = 0

    for marker, locations in markers.items():
        edges = collections.Counter()

        for location in locations:
            for offset in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                edges[(location * 2) + offset] += 1

        # print(edges)
        edge_set = set()

        for edge, count in edges.items():
            if count == 1:
                edge_set.add(edge)

        perimeter = len(edge_set)
        area = len(locations)

        print(f'marker {marker}: {perimeter} * {area} = {perimeter * area}')
        acc += perimeter * area



    # print(markers)
    return acc
    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
