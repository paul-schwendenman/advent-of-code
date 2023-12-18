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

direction_map = {
    "U": Direction.UP,
    "D": Direction.DOWN,
    "L": Direction.LEFT,
    "R": Direction.RIGHT,
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


def part1(data):
    grid = {}
    holes = set()
    location = Point(0, 0)
    grid[location] = None
    corners = [location]

    for line in data:
        match = re.match(r"([UDLR]) (\d+) \(\#([a-z0-9]+)\)", line)
        if not match:
            print(f'{line=}')
        direction, distance, color = match.groups()

        direction = direction_map[direction]
        distance = int(distance)

        for i in range(distance):
            location += direction
            grid[location] = color
        else:
            corners.append(location)

    # pprint.pprint(grid)

    print(f'{len(grid)}')

    max_x = max(item.x for item in grid.keys())
    min_x = min(item.x for item in grid.keys())
    max_y = max(item.y for item in grid.keys())
    min_y = min(item.y for item in grid.keys())

    print(f'{min_x}-{max_x} {min_y}-{max_y}')

    # for y in range(min_y, max_y+1):
    #     print(''.join("#" if (x, y) in grid else " " for x in range(min_x, max_x+1)))
    circumference = len(grid.keys())


    area = compute_polygonal_area(corners + [corners[0]])
    inner_points = compute_points_inside_polygon(area, circumference)

    return circumference + inner_points


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
