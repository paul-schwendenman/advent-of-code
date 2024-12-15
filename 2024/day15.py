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


def can_move(grid, robot, offset):
    next_space = robot + offset

    if grid[next_space] == '.':
        return True
    elif grid[next_space] == '#':
        return False

    return can_move(grid, robot + offset, offset)


def move(grid, robot, offset):
    if grid[robot + offset] == '#':
        raise ValueError('Can\'t move there')

    if grid[robot + offset] == '.':
        grid[robot + offset], grid[robot] = grid[robot], grid[robot + offset]
        return grid, robot + offset

    grid, _ = move(grid, robot + offset, offset)

    assert grid[robot + offset] == '.'
    grid[robot + offset], grid[robot] = grid[robot], grid[robot + offset]

    return grid, robot + offset


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

def can_move2(grid, robot, offset):
    next_space = robot + offset

    if grid[next_space] == '.':
        return True
    elif grid[next_space] == '#':
        return False
    elif grid[next_space] == '[' and offset in (Offset.UP, Offset.DOWN):
        return can_move2(grid, next_space, offset) and can_move2(grid, next_space + (1, 0), offset)
    elif grid[next_space] == '[' and offset in (Offset.LEFT, Offset.RIGHT):
        return can_move2(grid, next_space, offset)
    elif grid[next_space] == ']' and offset in (Offset.UP, Offset.DOWN):
        return can_move2(grid, next_space, offset) and can_move2(grid, next_space + (-1, 0), offset)
    elif grid[next_space] == ']' and offset in (Offset.LEFT, Offset.RIGHT):
        return can_move2(grid, next_space, offset)

    raise ValueError()


def move2(grid, robot, offset):
    if grid[robot + offset] == '#':
        raise ValueError('Can\'t move there')

    if grid[robot + offset] == '.':
        grid[robot + offset], grid[robot] = grid[robot], grid[robot + offset]
        return grid, robot + offset
    elif grid[robot + offset] == '[' and offset in (Offset.UP, Offset.DOWN):
        grid, _ = move2(grid, robot + offset, offset)
        grid, _ = move2(grid, robot + offset + (1, 0), offset)
        grid[robot + offset], grid[robot] = grid[robot], grid[robot + offset]

        return grid, robot + offset
    elif grid[robot + offset] == ']' and offset in (Offset.UP, Offset.DOWN):
        grid, _ = move2(grid, robot + offset, offset)
        grid, _ = move2(grid, robot + offset + (-1, 0), offset)
        grid[robot + offset], grid[robot] = grid[robot], grid[robot + offset]

        return grid, robot + offset

    grid, _ = move2(grid, robot + offset, offset)

    assert grid[robot + offset] == '.'
    grid[robot + offset], grid[robot] = grid[robot], grid[robot + offset]

    return grid, robot + offset

def part1(data):
    parts = ''.join(line for line in data).split('\n\n')

    grid, j, k, markers = parse_grid(parts[0].split('\n'))
    instructions = parts[1].rstrip()

    # print(f'instructions: {instructions}')
    robot = markers['@'][0]

    print('Initial state:')
    print_grid(grid, j, k)
    print('')

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

        print(f'Move {instruction}:')
        print_grid(grid, j, k)
        print('')

    return sum(100 * y + x for (x, y), value in grid.items() if value=='O')

    pass


def part2(data):
    parts = ''.join(line for line in data).split('\n\n')

    half_grid, j, k, _ = parse_grid(parts[0].split('\n'))
    instructions = parts[1].rstrip()

    # print(f'instructions: {instructions}')
    grid, robot = double_grid(half_grid)
    j = j * 2 + 1

    print('Initial state:')
    print_grid(grid, j, k)
    print('')

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

        print(f'Move {instruction}:')

        if can_move2(grid, robot, offset):
            grid, robot = move2(grid, robot, offset)

        print_grid(grid, j, k)
        print('')

    return sum(100 * y + x for (x, y), value in grid.items() if value=='O')
    pass


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
