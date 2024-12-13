import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing

def extract_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))


def parse_input(data):
    lines = [line.rstrip() for line in data]

    everything = '|'.join(lines)
    raw_machines = everything.split('||')

    machines = []

    for raw_machine in raw_machines:
        (a_x, a_y, b_x, b_y, goal_x, goal_y) = extract_ints(raw_machine)

        machines.append((a_x, a_y, b_x, b_y, goal_x, goal_y))

    return machines


def simulate_machine(machine, offset=0):
    (a_x, a_y, b_x, b_y, goal_x, goal_y) = machine
    # a_x * a + b_x * b = goal_x
    # a_y * a + b_y * b = goal_y
    # a = goal_x / a_x - (b_x * b) / a_x
    # a = (goal_x - b_x * b) / a_x
    # b = (goal_x - a_x * a) / b_x
    # b = (goal_y - a_y * a) / b_y

    # print(f'{goal_x} {goal_y}')

    goal_y += offset
    goal_x += offset

    #         (goal_x - a_x * a) / b_x = (goal_y - a_y * a) / b_y
    #         (goal_x - a_x * a) * b_y = (goal_y - a_y * a) * b_x
    #   (goal_x * b_y - a_x * b_y * a) = (goal_y * b_x - a_y * a * b_x)
    #  - a_x * b_y * a + a_y * a * b_x = goal_y * b_x - goal_x * b_y
    #    (- a_x * b_y + a_y * b_x) * a = goal_y * b_x - goal_x * b_y
    #      (a_y * b_x - a_x * b_y) * a = goal_y * b_x - goal_x * b_y
    #                                a = (goal_y * b_x - goal_x * b_y) / (a_y * b_x - a_x * b_y)

    a = (goal_y * b_x - goal_x * b_y) // (a_y * b_x - a_x * b_y)

    # b
    # b = (goal_y - a_y * a) / b_y

    b = (goal_y - a_y * a) // b_y

    # print(f'x: {goal_x} = {a * a_x + b * b_x} = {a} * {a_x} + {b} * {b_x}')
    # print(f'y: {goal_y} = {a * a_y + b * b_y} = {a} * {a_y} + {b} * {b_y}')
    # print(f'tokens: {a:3d} * 3 + {b:3d} = {a * 3 + b}')

    if goal_x == a * a_x + b * b_x and goal_y == a * a_y + b * b_y:
        return a * 3 + b
    else:
        return 0



def part1(data):
    machines = parse_input(data)
    tokens = 0

    for machine in machines:
        tokens += simulate_machine(machine)

    return tokens
    pass


def part2(data):
    machines = parse_input(data)
    tokens = 0

    for machine in machines:
        tokens += simulate_machine(machine, 10000000000000)

    return tokens
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
