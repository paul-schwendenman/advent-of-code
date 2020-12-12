from __future__ import annotations
from typing import cast, List, Tuple
from aoc import readfile
from collections import namedtuple
from enum import Enum

Rotation = Tuple[Tuple[int, int], Tuple[int, int]]


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

    def __matmul__(self: Point, other: Rotation) -> Waypoint:
        x = self.x * other[0][0] + self.y * other[0][1]
        y = self.x * other[1][0] + self.y * other[1][1]

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


def map_angle_to_rotation(angle: int) -> Rotation:
    return {
        0: ((1, 0), (0, 1)),
        90: ((0, -1), (1, 0)),
        180: ((-1, 0), (0, -1)),
        270: ((0, 1), (-1, 0)),
    }[angle % 360]


def parse_command(command: str) -> Tuple[Action, int]:
    return Action(command[0]), int(command[1:])


def part1(data: List[str]) -> int:
    ship = Point(0, 0)
    theta = 0

    for command in data:
        action, num = parse_command(command)

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
        action, num = parse_command(command)

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
            rotation = map_angle_to_rotation(num)
            waypoint @= rotation
        elif action == Action.RIGHT:
            rotation = map_angle_to_rotation(-num)
            waypoint @= rotation

    return ship.manhattan_distance()


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
