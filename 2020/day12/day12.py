from __future__ import annotations
from typing import cast, List, Tuple
from aoc import readfile
from collections import namedtuple
from enum import Enum


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def __add__(self: Point, other: Tuple) -> Point:
        return Point(self.x + other[0], self.y + other[1])

    def manhattan_distance(self) -> int:
        return cast(int, abs(self.x) + abs(self.y))


class Waypoint(Point):
    def __add__(self: Point, other: Tuple) -> Waypoint:
        return Waypoint(self.x + other[0], self.y + other[1])

    def __mul__(self: Point, other: int) -> Waypoint:
        return Waypoint(self.x * other, self.y * other)

    def rotate(self, angle: int) -> Waypoint:
        angle = angle % 360
        if angle == 90:
            x, y = -self.y, self.x
        elif angle == 180:
            x, y = -self.x, -self.y
        elif angle == 270:
            x, y = self.y, -self.x

        return Waypoint(x, y)


class Action(Enum):
    FORWARD = 'F'
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'
    RIGHT = 'R'
    LEFT = 'L'


def map_angle_to_action(angle: int) -> Action:
    return {
        0: Action.EAST,
        90: Action.NORTH,
        180: Action.WEST,
        270: Action.SOUTH,
    }[angle % 360]


def part1(data: List[str]) -> int:
    ship = Point(0, 0)
    theta = 0

    for command in data:
        action, num = Action(command[0]), int(command[1:])

        if action == Action.FORWARD:
            action = map_angle_to_action(theta)

        if action == Action.NORTH:
            ship += (0, -num)
        elif action == Action.SOUTH:
            ship += (0, num)
        elif action == Action.WEST:
            ship += (-num, 0)
        elif action == Action.EAST:
            ship += (num, 0)
        elif action == Action.LEFT:
            theta += num
        elif action == Action.RIGHT:
            theta -= num

    return ship.manhattan_distance()


def part2(data: List[str]) -> int:
    ship = Point(0, 0)
    waypoint = Waypoint(10, 1)

    for command in data:
        action, num = Action(command[0]), int(command[1:])

        if action == Action.FORWARD:
            ship += waypoint * num
        elif action == Action.NORTH:
            waypoint += (0, num)
        elif action == Action.SOUTH:
            waypoint += (0, -num)
        elif action == Action.WEST:
            waypoint += (-num, 0)
        elif action == Action.EAST:
            waypoint += (num, 0)
        elif action == Action.LEFT:
            waypoint = waypoint.rotate(num)
        elif action == Action.RIGHT:
            waypoint = waypoint.rotate(-num)

    return ship.manhattan_distance()


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
