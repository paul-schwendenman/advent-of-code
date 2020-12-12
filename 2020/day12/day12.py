from __future__ import annotations
from typing import List
from aoc import readfile
# from math import


def part1(data: List[str]) -> int:
    x = 0
    y = 0
    theta = 0

    for command in data:
        action, num = command[0], int(command[1:])

        if action == 'F':
            action = {
                0: 'E',
                90: 'N',
                180: 'W',
                270: 'S'
            }[theta % 360]

        if action == 'N':
            y -= num
        elif action == 'S':
            y += num
        elif action == 'W':
            x -= num
        elif action == 'E':
            x += num
        elif action == 'L':
            theta += num
        elif action == 'R':
            theta -= num

    return abs(x) + abs(y)


def part2(data: List[str]) -> int:
    x = 0
    w_x = 10
    y = 0
    w_y = 1

    for command in data:
        action, num = command[0], int(command[1:])

        if action == 'F':
            x += w_x * num
            y += w_y * num

        if action == 'N':
            w_y += num
        elif action == 'S':
            w_y -= num
        elif action == 'W':
            w_x -= num
        elif action == 'E':
            w_x += num
        elif action == 'L':
            if num == 90:
                w_y, w_x = w_x, -w_y
            elif num == 180:
                w_y, w_x = -w_y, -w_x
            elif num == 270:
                w_y, w_x = -w_x, w_y

        elif action == 'R':
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
