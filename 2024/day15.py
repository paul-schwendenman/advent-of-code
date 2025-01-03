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

class Spot(enum.Enum):
    ROBOT = '@'
    EMPTY = '.'
    WALL = '#'
    BOX = 'O'
    LEFT_BOX = '['
    RIGHT_BOX = ']'

    def __eq__(self, other):
        return self.value == other

    @classmethod
    def GPS_TAGS(cls):
        return (cls.LEFT_BOX, cls.BOX)


def parse_input(data):
    parts = ''.join(line for line in data).split('\n\n')

    grid, _, _, markers = parse_grid(parts[0].split('\n'))
    instructions = parts[1].rstrip()

    return grid, markers, instructions


def print_grid(grid, max_x, max_y):
    for j in range(0, max_y+1):
        print("".join(grid.get((i, j), Spot.EMPTY) for i in range(0, max_x+1)))


def double_grid(grid):
    new_grid: Dict[Point, str] = {}
    robot = None

    for space, value in grid.items():
        left = Point(space.x * 2, space.y)
        right = Point(space.x * 2 + 1, space.y)

        match value:
            case Spot.ROBOT:
                new_grid[left] = Spot.ROBOT
                new_grid[right] = Spot.EMPTY
                robot = left
            case Spot.WALL:
                new_grid[left] = Spot.WALL
                new_grid[right] = Spot.WALL
            case Spot.BOX:
                new_grid[left] = Spot.LEFT_BOX
                new_grid[right] = Spot.RIGHT_BOX
            case Spot.EMPTY:
                new_grid[left] = Spot.EMPTY
                new_grid[right] = Spot.EMPTY

    return new_grid, robot


def can_move(grid, location, offset):
    next_location = location + offset

    match grid[next_location], offset:
        case Spot.EMPTY, _:
            return True
        case Spot.WALL, _:
            return False
        case Spot.BOX, _:
            return can_move(grid, next_location, offset)
        case Spot.LEFT_BOX, Offset.UP | Offset.DOWN:
            return can_move(grid, next_location, offset) and can_move(grid, next_location + Offset.RIGHT, offset)
        case Spot.LEFT_BOX, Offset.LEFT | Offset.RIGHT:
            return can_move(grid, next_location, offset)
        case Spot.RIGHT_BOX, Offset.UP | Offset.DOWN:
            return can_move(grid, next_location, offset) and can_move(grid, next_location + Offset.LEFT, offset)
        case Spot.RIGHT_BOX, Offset.LEFT | Offset.RIGHT:
            return can_move(grid, next_location, offset)

    raise ValueError()


def move(grid, location, offset):
    next_location = location + offset
    if grid[next_location] == Spot.WALL:
        raise ValueError("Can't move there")

    if grid[next_location] == Spot.EMPTY:
        grid[next_location], grid[location] = grid[location], grid[next_location]
        return grid, next_location
    elif grid[next_location] == Spot.LEFT_BOX and offset in (Offset.UP, Offset.DOWN):
        grid, _ = move(grid, next_location, offset)
        grid, _ = move(grid, next_location + Offset.RIGHT, offset)
        grid[next_location], grid[location] = grid[location], grid[next_location]

        return grid, next_location
    elif grid[next_location] == Spot.RIGHT_BOX and offset in (Offset.UP, Offset.DOWN):
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


def score_gps(grid):
    return sum(100 * y + x for (x, y), value in grid.items() if value in Spot.GPS_TAGS())


def part1(data):
    map, markers, instructions = parse_input(data)
    robot = markers[Spot.ROBOT.value][0]

    final_map = simulate_instructions(map, robot, instructions)

    return score_gps(final_map)


def part2(data):
    half_map, _, instructions = parse_input(data)

    map, robot = double_grid(half_map)

    final_map = simulate_instructions(map, robot, instructions)

    return score_gps(final_map)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
