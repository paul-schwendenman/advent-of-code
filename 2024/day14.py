import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def print_grid(robots, max_x, max_y):
    c = collections.Counter((robot[0], robot[1]) for robot in robots)

    for j in range(max_y):
        for k in range(max_x):
            if (k, j) in c:
                print(c[(k, j)], end='')
            else:
                print('.', end='')
        print('')

    print('')

def extract_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))


def parse_robot(line):
    x, y, dx, dy = extract_ints(line)

    return (x, y, dx, dy)


def part1(data, max_x=101, max_y=103):
    robots = [parse_robot(line) for line in data]

    # print_grid(robots, max_x, max_y)

    # print(robots[0])

    for step in range(100):
        # print(f'------ {step} --------')
        new_robots = []

        for robot in robots:
            x, y, dx, dy = robot
            new_robot = ((x + dx) % max_x, (y + dy) % max_y, dx, dy)

            new_robots.append(new_robot)
            pass

        robots = new_robots
        # print_grid(robots, max_x, max_y)

    # print_grid(robots, max_x, max_y)
    q1 = len([1 for robot in robots if robot[0] < max_x // 2 and robot[1] < max_y // 2])
    q2 = len([1 for robot in robots if robot[0] > max_x // 2 and robot[1] < max_y // 2])
    q3 = len([1 for robot in robots if robot[0] < max_x // 2 and robot[1] > max_y // 2])
    q4 = len([1 for robot in robots if robot[0] > max_x // 2 and robot[1] > max_y // 2])

    # print(f'{q1} * {q2} * {q3} * {q4} = {q1 * q2 * q3 * q4}')

    return q1 * q2 * q3 * q4

    pass


def part2(data, max_x=101, max_y=103):
    robots = [parse_robot(line) for line in data]
    num_robots = len(robots)

    for step in itertools.count(1):
        new_robots = []

        for robot in robots:
            x, y, dx, dy = robot
            new_robot = ((x + dx) % max_x, (y + dy) % max_y, dx, dy)

            new_robots.append(new_robot)
            pass

        robots = new_robots

        if num_robots == len(set((x, y) for x, y, _, _ in robots)):
            break

    return step


def main():
    # print(part1(fileinput.input(), 11, 7))
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
