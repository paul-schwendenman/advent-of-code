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
    grid, _, _, antennas = parse_grid(data, exclude='.#')

    antinodes = set()

    for _, locations in antennas.items():
        for a, b in itertools.permutations(locations, r=2):
            diff = b - a
            next_location = b + diff

            if next_location in grid:
                antinodes.add(next_location)

    return len(antinodes)


def part2(data):
    grid, _, _, antennas = parse_grid(data, exclude=".#")

    antinodes = set()

    for _, locations in antennas.items():
        for a, b in itertools.permutations(locations, r=2):
            diff = b - a

            next_location = b
            while next_location in grid:
                antinodes.add(next_location)

                next_location = next_location + diff
    return len(antinodes)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
