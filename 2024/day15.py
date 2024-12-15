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


def print_grid(grid, max_x, max_y):
    for j in range(0, max_y+1):
        print("".join(grid.get((i, j), '.') for i in range(0, max_x+1)))


def double_grid(grid):
    new_grid: Dict[Point, str] = {}
    robot = None

    for space, value in grid.items():
        left = Point(space.x * 2, space.y)
        right = Point(space.x * 2 + 1, space.y)

        if value == '@':
            new_grid[left] = '@'
            new_grid[right] = '.'
            robot = left
        if value == '#':
            new_grid[left] = '#'
            new_grid[right] = '#'
        if value == 'O':
            new_grid[left] = '['
            new_grid[right] = ']'
        if value == '.':
            new_grid[left] = '.'
            new_grid[right] = '.'

    return new_grid, robot


def can_move(grid, location, offset):
    next_location = location + offset

    if grid[next_location] == '.':
        return True
    elif grid[next_location] == '#':
        return False
    elif grid[next_location] == 'O':
        return can_move(grid, next_location, offset)
    elif grid[next_location] == '[' and offset in (Offset.UP, Offset.DOWN):
        return can_move(grid, next_location, offset) and can_move(grid, next_location + Offset.RIGHT, offset)
    elif grid[next_location] == '[' and offset in (Offset.LEFT, Offset.RIGHT):
        return can_move(grid, next_location, offset)
    elif grid[next_location] == ']' and offset in (Offset.UP, Offset.DOWN):
        return can_move(grid, next_location, offset) and can_move(grid, next_location + Offset.LEFT, offset)
    elif grid[next_location] == ']' and offset in (Offset.LEFT, Offset.RIGHT):
        return can_move(grid, next_location, offset)

    raise ValueError()


def move(grid, location, offset):
    next_location = location + offset
    if grid[next_location] == '#':
        raise ValueError("Can't move there")

    if grid[next_location] == '.':
        grid[next_location], grid[location] = grid[location], grid[next_location]
        return grid, next_location
    elif grid[next_location] == '[' and offset in (Offset.UP, Offset.DOWN):
        grid, _ = move(grid, next_location, offset)
        grid, _ = move(grid, next_location + Offset.RIGHT, offset)
        grid[next_location], grid[location] = grid[location], grid[next_location]

        return grid, next_location
    elif grid[next_location] == ']' and offset in (Offset.UP, Offset.DOWN):
        grid, _ = move(grid, next_location, offset)
        grid, _ = move(grid, next_location + Offset.LEFT, offset)
        grid[next_location], grid[location] = grid[location], grid[next_location]

        return grid, next_location

    grid, _ = move(grid, next_location, offset)
    grid[next_location], grid[location] = grid[location], grid[next_location]

    return grid, next_location


def simulate_instructions(grid, robot, instructions):
    for instruction in instructions:
        if instruction == '<':
            offset = Offset.LEFT
        elif instruction == '>':
            offset = Offset.RIGHT
        elif instruction == '^':
            offset = Offset.UP
        elif instruction == 'v':
            offset = Offset.DOWN
        elif instruction == '\n':
            continue
        else:
            raise ValueError(f'Unknown instruction: "{instruction}"')

        if can_move(grid, robot, offset):
            grid, robot = move(grid, robot, offset)

    return grid


def part1(data):
    parts = ''.join(line for line in data).split('\n\n')

    grid, j, k, markers = parse_grid(parts[0].split('\n'))
    instructions = parts[1].rstrip()

    robot = markers['@'][0]

    grid = simulate_instructions(grid, robot, instructions)

    return sum(100 * y + x for (x, y), value in grid.items() if value=='O')


def part2(data):
    parts = ''.join(line for line in data).split('\n\n')

    half_grid, j, k, _ = parse_grid(parts[0].split('\n'))
    instructions = parts[1].rstrip()

    grid, robot = double_grid(half_grid)
    j = j * 2 + 1

    grid = simulate_instructions(grid, robot, instructions)

    return sum(100 * y + x for (x, y), value in grid.items() if value=='[')


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
