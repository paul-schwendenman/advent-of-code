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

    def get_neighbors(self):
        # for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1),):
            yield self + offset

    def get_neighbors_fancy(self):
        # for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
        for offset, dir in (((-1, 0), 'L'), ((1, 0), 'R'), ((0, -1), 'U'), ((0, 1), 'D'),):
            yield self + offset, dir

    def get_neighbors_directional(self, dir):
        if dir == '-':
            for offset in ((-1, 0), (1, 0)):
                yield self + offset
        elif dir == '|':
            for offset in ((0, -1), (0, 1)):
                yield self + offset

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


def find_regions(grid, markers):
    for marker, locations in markers.items():
        # print(f'marker {marker}')
        sets = {location: {location} for location in locations}

        # print(sets)

        for location in locations:
            for neighbor in location.get_neighbors():
                if neighbor in locations:
                    # print(f'{location} -> {neighbor}: {grid[location]}=={grid[neighbor]}')
                    sets[location] |= sets[neighbor]

                    for joined in sets[location]:
                        sets[joined] = sets[location]

        # print(sets)

        for group in {tuple(group) for group in sets.values()}:
            # print(f'yielding: {marker} {group}')
            yield (marker, group)


def part1(data):
    grid, _, _, markers = parse_grid(data)
    acc = 0

    # pprint.pprint(list(find_regions(grid, markers)))

    for marker, locations in find_regions(grid, markers):
    # for marker, locations in markers.items():
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

        # print(f'marker {marker}: {perimeter} * {area} = {perimeter * area}')
        acc += perimeter * area

    # print(markers)
    return acc
    pass

def get_all_neighbors(locations):
    for location in locations:
        for neighbor, dir in location.get_neighbors_fancy():
            if neighbor not in locations:
                yield neighbor, dir


def part2(data):
    grid, _, _, markers = parse_grid(data)
    acc = 0

    # pprint.pprint(list(find_regions(grid, markers)))

    for marker, locations in find_regions(grid, markers):
        # print(f'---- {marker} ----')
        # print(f'{locations}')
        all_neighbors = list(get_all_neighbors(locations))
        # print(f'n: {all_neighbors}')

        sets = {neighbor: {neighbor} for neighbor in all_neighbors}

        for location, dir in all_neighbors:
            for neighbor in location.get_neighbors():
                if (neighbor, dir) in all_neighbors:
                    sets[(location, dir)] |= sets[(neighbor, dir)]

                    for joined in sets[(location, dir)]:
                        sets[joined] = sets[(location, dir)]


        lines = {tuple(group) for group in sets.values()}

        # pprint.pprint(lines)

        perimeter = len(lines)
        # perimeter = len(all_neighbors)
        area = len(locations)

        print(f'marker {marker}: {perimeter} * {area} = {perimeter * area}')
        acc += perimeter * area

    # print(markers)
    return acc
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
