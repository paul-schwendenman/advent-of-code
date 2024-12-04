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

    def get_neighbors(self):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

class Offset(enum.Enum):
    TOP_LEFT = (-1, -1)
    TOP_RIGHT = (-1, 1)
    BOTTOM_LEFT = (1, -1)
    BOTTOM_RIGHT = (1, 1)

    def __mul__(self, scalar):
        return (self.value[0] * scalar, self.value[1] * scalar)

    def __getitem__(self, index):
        return self.value[index]


def make_grid(lines):
    grid = collections.defaultdict(str)
    xs = set()
    a_s = set()

    for y, line in enumerate(lines):
        for x, char in enumerate(line.rstrip()):
            grid[Point(x, y)] = char
            if char == 'X':
                xs.add(Point(x,y))
            if char == 'A':
                a_s.add(Point(x, y))



    return grid, xs, a_s

def part1(data):
    grid, xs, _ = make_grid(data)

    found = 0

    for x in xs:
        for offset in (Offset.TOP_RIGHT, Offset.TOP_LEFT, Offset.BOTTOM_LEFT, Offset.BOTTOM_RIGHT):
            if grid[x + offset] == 'M' and grid[x + offset * 2] == 'A' and grid[x + offset * 3] == 'S':
                found += 1

    return found


def part2(data):
    grid, _, a_s = make_grid(data)

    found = 0

    for a in a_s:
        if grid[a + (1, 1)] == 'S' and grid[a+ (-1, 1)] == 'S' and grid[a + (1, -1)] == 'M' and grid[a + (-1, -1)] == 'M':
            found += 1
        if grid[a + (1, 1)] == 'M' and grid[a+ (-1, 1)] == 'M' and grid[a + (1, -1)] == 'S' and grid[a + (-1, -1)] == 'S':
            found += 1
        if grid[a + (1, 1)] == 'S' and grid[a+ (-1, 1)] == 'M' and grid[a + (1, -1)] == 'S' and grid[a + (-1, -1)] == 'M':
            found += 1
        if grid[a + (1, 1)] == 'M' and grid[a+ (-1, 1)] == 'S' and grid[a + (1, -1)] == 'M' and grid[a + (-1, -1)] == 'S':
            found += 1

    return found


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
