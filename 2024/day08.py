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


def parse_grid(data):
    grid = {}
    antennas = collections.defaultdict(list)

    for j, line in enumerate(data):
        for i, char in enumerate(line.rstrip()):
            here = Point(i, j)

            grid[here] = char

            if char not in '.#':
                antennas[char].append(here)

    return grid, i, j, antennas

def part1(data):
    grid, i, j, antennas = parse_grid(data)

    antinodes = set()

    for key, locations in antennas.items():
        for a, b in itertools.permutations(locations, r=2):
            diff = b - a
            next_location = b + diff

            if 0 <= next_location[0] <= i and 0 <= next_location[1] <= j:
                antinodes.add(next_location)


    return len(antinodes)
    pass


def part2(data):
    grid, i, j, antennas = parse_grid(data)
    # print(i,j)

    antinodes = set()

    for key, locations in antennas.items():
        for a, b in itertools.permutations(locations, r=2):
            antinodes.add(b)
            diff = b - a

            next_location = b + diff
            while 0 <= next_location[0] <= i and 0 <= next_location[1] <= j:
                antinodes.add(next_location)

                next_location = next_location + diff
    return len(antinodes)
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
