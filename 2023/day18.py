import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


class Point(typing.NamedTuple):
    x: int
    y: int

    def get_neighbors(self):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])


class Direction(tuple, enum.Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def __mul__(self, num):
        return (self[0] * num, self[1] * num)


direction_map = {
    "U": Direction.UP,
    "D": Direction.DOWN,
    "L": Direction.LEFT,
    "R": Direction.RIGHT,
    "3": Direction.UP,
    "1": Direction.DOWN,
    "2": Direction.LEFT,
    "0": Direction.RIGHT,
}


def compute_polygonal_area(vertices):
    # Triangle formula to compute area of a polygon
    # https://en.m.wikipedia.org/wiki/Shoelace_formula#Triangle_formula
    area = 0
    for point_a, point_b in itertools.pairwise(vertices):
        area += point_a.x * point_b.y - point_a.y * point_b.x

    return abs(area / 2)


def compute_points_inside_polygon(area, num_edges):
    # Pick's theorem to compute the inner points of a grid-based polygon
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    return int(area - num_edges / 2 + 1)


def parse_data(data):
    for line in data:
        match = re.match(r"([UDLR]) (\d+) \(\#([a-z0-9]+)\)", line)
        if not match:
            print(f'{line=}')
        yield match.groups()


def parse_directions(data):
    for direction, distance, _ in parse_data(data):
        yield direction_map[direction], int(distance)


def parse_colors(data):
    for _, _, color in parse_data(data):
        direction = direction_map[color[-1]]
        distance = int(color[:5], 16)

        yield direction, distance


def part1(data):
    location = Point(0, 0)
    corners = [location]
    circumference = 0

    for direction, distance in parse_directions(data):
        circumference += distance

        location += direction * distance

        corners.append(location)

    area = compute_polygonal_area(corners + [corners[0]])
    inner_points = compute_points_inside_polygon(area, circumference)

    return circumference + inner_points


def part2(data):
    location = Point(0, 0)
    corners = [location]
    circumference = 0

    for direction, distance in parse_colors(data):
        circumference += distance
        location += direction * distance

        corners.append(location)

    area = compute_polygonal_area(corners + [corners[0]])
    inner_points = compute_points_inside_polygon(area, circumference)

    return circumference + inner_points


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
