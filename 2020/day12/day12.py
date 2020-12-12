from __future__ import annotations
from typing import List
from aoc import readfile
from enum import Enum


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
    x = 0
    y = 0
    theta = 0

    for command in data:
        action, num = Action(command[0]), int(command[1:])

        if action == Action.FORWARD:
            action = map_angle_to_action(theta)

        if action == Action.NORTH:
            y -= num
        elif action == Action.SOUTH:
            y += num
        elif action == Action.WEST:
            x -= num
        elif action == Action.EAST:
            x += num
        elif action == Action.LEFT:
            theta += num
        elif action == Action.RIGHT:
            theta -= num

    return abs(x) + abs(y)


def part2(data: List[str]) -> int:
    x = 0
    w_x = 10
    y = 0
    w_y = 1

    for command in data:
        action, num = Action(command[0]), int(command[1:])

        if action == Action.FORWARD:
            x += w_x * num
            y += w_y * num

        if action == Action.NORTH:
            w_y += num
        elif action == Action.SOUTH:
            w_y -= num
        elif action == Action.WEST:
            w_x -= num
        elif action == Action.EAST:
            w_x += num
        elif action == Action.LEFT:
            if num == 90:
                w_y, w_x = w_x, -w_y
            elif num == 180:
                w_y, w_x = -w_y, -w_x
            elif num == 270:
                w_y, w_x = -w_x, w_y

        elif action == Action.RIGHT:
            if num == 90:
                w_y, w_x = -w_x, w_y
            elif num == 180:
                w_y, w_x = -w_y, -w_x
            elif num == 270:
                w_y, w_x = w_x, -w_y

    return abs(x) + abs(y)


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
