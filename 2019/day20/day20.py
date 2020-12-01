from __future__ import annotations
from typing import Dict, Iterator, Set
from collections import namedtuple, defaultdict
import itertools


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighboors(self) -> Iterator[Point]:
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            yield self + offset

    def __add__(self, other) -> Point:
        return Point(self.x + other[0], self.y + other[1])


def get_portal_neighboor(base_point: Point, template) -> Point:
    def check_char(point):
        try:
            return template[point.y][point.x].isalpha()
        except IndexError:
            return False

    neighboors = filter(check_char, base_point.get_neighboors())

    return next(neighboors)


def get_portal_name(base_point: Point, template) -> str:
    neighboor = get_portal_neighboor(base_point, template)

    first_char = template[min(base_point.y, neighboor.y)][min(base_point.x, neighboor.x)]
    second_char = template[max(base_point.y, neighboor.y)][max(base_point.x, neighboor.x)]
    return first_char + second_char


def get_portal_location(base_point: Point, template) -> Point:
    def check_char(point):
        try:
            return template[point.y][point.x] == '.'
        except IndexError:
            return False

    neighboor = get_portal_neighboor(base_point, template)
    possible_locations = itertools.chain(base_point.get_neighboors(), neighboor.get_neighboors())

    location = filter(check_char, possible_locations)

    return next(location)


def process_maze(maze_template):
    maze: Dict[Point, str] = {}
    portals: Dict[str, Set[Point]] = defaultdict(set)

    for y, row in enumerate(maze_template):
        for x, cell in enumerate(row):
            point = Point(x, y)
            maze[point] = cell
            if cell.isalpha():
                portal_name = get_portal_name(point, maze_template)
                portal_location = get_portal_location(point, maze_template)
                portals[portal_name].add(portal_location)

    return maze, portals


def main(filename='input'):
    with open(filename) as input_file:
        maze_template = input_file.read().splitlines()

    return process_maze(maze_template)[1]


if __name__ == "__main__":
    print(main('example1.input'))
