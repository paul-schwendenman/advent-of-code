import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from utils import Point, Offset, parse_grid


def get_neighbors_fancy(point: Point):
    # for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
    for offset, dir in (((-1, 0), 'L'), ((1, 0), 'R'), ((0, -1), 'U'), ((0, 1), 'D'),):
        yield point + offset, dir


def find_regions(markers: typing.Dict[str, list[Point]]):
    for marker, locations in markers.items():
        sets = {location: {location} for location in locations}

        for location in locations:
            for neighbor in location.get_neighbors(offsets=Offset.cardinal()):
                if neighbor in locations:
                    sets[location] |= sets[neighbor]

                    for joined in sets[location]:
                        sets[joined] = sets[location]

        for group in {tuple(group) for group in sets.values()}:
            yield (marker, group)


def price_region(locations):
    edges = set(get_all_neighbors(locations))

    perimeter = len(edges)
    area = len(locations)

    return perimeter * area


def part1(data):
    _, _, _, markers = parse_grid(data)

    return sum(price_region(region) for _, region in find_regions(markers))


def get_all_neighbors(locations):
    for location in locations:
        for neighbor, dir in get_neighbors_fancy(location):
            if neighbor not in locations:
                yield neighbor, dir


def part2(data):
    grid, _, _, markers = parse_grid(data)
    acc = 0

    for marker, locations in find_regions(markers):
        all_neighbors = list(get_all_neighbors(locations))

        sets = {neighbor: {neighbor} for neighbor in all_neighbors}

        for location, dir in all_neighbors:
            for neighbor in location.get_neighbors(offsets=Offset.cardinal()):
                if (neighbor, dir) in all_neighbors:
                    sets[(location, dir)] |= sets[(neighbor, dir)]

                    for joined in sets[(location, dir)]:
                        sets[joined] = sets[(location, dir)]

        lines = {tuple(group) for group in sets.values()}

        perimeter = len(lines)
        area = len(locations)

        acc += perimeter * area

    return acc


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
