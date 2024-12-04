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
        return (self.value[0] * scalar, self.value[1] * scalar)

    def __getitem__(self, index):
        return self.value[index]

    def __eq__(self, tuple):
        return len(tuple) == 2 and self.value[0] == tuple[0] and self.value[1] == tuple[1]

    @classmethod
    def cardinal(cls):
        return (cls.UP, cls.LEFT, cls.RIGHT, cls.DOWN)

    @classmethod
    def diagonal(cls):
        return (cls.TOP_LEFT, cls.TOP_RIGHT, cls.BOTTOM_LEFT, cls.BOTTOM_RIGHT)

    @classmethod
    def all(cls):
        return cls.cardinal() + cls.diagonal()


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

def find_word(grid, location, word, direction, start=0):
    for index, char in enumerate(word, start=start):
        if grid.get(location + direction * index) == char:
            continue
        break
    else:
        return True

    return False

def part1(data):
    grid, xs, _ = make_grid(data)

    found = 0

    for x in xs:
        for offset in Offset.all():
            if find_word(grid, x, 'XMAS', offset):
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
