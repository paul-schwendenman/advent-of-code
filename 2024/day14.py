import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from utils import *

MAX_X, MAX_Y = 101, 103

class Robot(collections.namedtuple('Robot', 'x y dx dy')):
    __slots__ = ()

    def move(self, max_x=MAX_X, max_y=MAX_Y):
        return Robot((self.x + self.dx) % max_x, (self.y + self.dy) % max_y, self.dx, self.dy)



def print_grid(robots: list[Robot], max_x: int, max_y: int):
    c = collections.Counter((robot[0], robot[1]) for robot in robots)

    for j in range(max_y):
        for k in range(max_x):
            if (k, j) in c:
                print(c[(k, j)], end='')
            else:
                print('.', end='')
        print('')

    print('')


def parse_robot(line: str) -> Robot:
    x, y, dx, dy = extract_ints(line)

    return Robot(x, y, dx, dy)


def parse_robots(data) -> list[Robot]:
    return [parse_robot(line) for line in data]


def move_robots(robots: list[Robot], *, max_x: int = MAX_X, max_y: int = MAX_Y) -> list[Robot]:
    return [robot.move(max_x, max_y) for robot in robots]


def count_quadrants(robots: list[Robot], *, max_x: int = MAX_X, max_y: int = MAX_Y) -> tuple[int, int, int, int]:
    q1 = len([1 for robot in robots if robot[0] < max_x // 2 and robot[1] < max_y // 2])
    q2 = len([1 for robot in robots if robot[0] > max_x // 2 and robot[1] < max_y // 2])
    q3 = len([1 for robot in robots if robot[0] < max_x // 2 and robot[1] > max_y // 2])
    q4 = len([1 for robot in robots if robot[0] > max_x // 2 and robot[1] > max_y // 2])

    return (q1, q2, q3, q4)


def part1(data, max_x=MAX_X, max_y=MAX_Y):
    robots = parse_robots(data)

    for _ in range(100):
        robots = move_robots(robots, max_x=max_x, max_y=max_y)

    quadrants = count_quadrants(robots=robots, max_x=max_x, max_y=max_y)

    return math.prod(quadrants)


def part2(data):
    robots = parse_robots(data)

    num_robots = len(robots)

    for step in itertools.count(1):
        robots = move_robots(robots)

        if num_robots == len(set((x, y) for x, y, _, _ in robots)):
            break

    return step


def main():
    # print(part1(fileinput.input(), 11, 7))
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
