from intcode import IntCode, open_program
from collections import defaultdict, namedtuple
from enum import IntEnum
from copy import deepcopy
import sys


sys.setrecursionlimit(5500000)


Point = namedtuple('Point', 'x y')


class Direction(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class StatusCode(IntEnum):
    WALL = 0
    MOVED = 1
    FOUND = 2


class GridSpace(IntEnum):
    UNKNOWN = 0
    EMPTY = 1
    WALL = 2
    DROID = 3
    OXYGEN_SYSTEM = 4


def get_next_square(current_location: Point, direction: Direction):
    if direction == Direction.NORTH:
        return Point(current_location.x - 1, current_location.y)
    elif direction == Direction.SOUTH:
        return Point(current_location.x + 1, current_location.y)
    elif direction == Direction.EAST:
        return Point(current_location.x, current_location.y - 1)
    elif direction == Direction.WEST:
        return Point(current_location.x, current_location.y + 1)


def run_move(computer, move, grid, location, depth):
    oxygen_found = 1e15
    next_location = get_next_square(location, move)
    if next_location in grid:
        return grid, oxygen_found
    computer = deepcopy(computer)
    computer.add_input(move)

    computer.run()

    output = computer.get_output()

    if output == StatusCode.WALL:
        grid[next_location] = GridSpace.WALL
    elif output == StatusCode.MOVED:
        grid[next_location] = GridSpace.EMPTY
        location = next_location
        grid, oxygen_found = run_moves(computer, grid, next_location, depth+1)
    elif output == StatusCode.FOUND:
        grid[next_location] = GridSpace.OXYGEN_SYSTEM
        oxygen_found = depth
        print(f'found OXY at {next_location}')
    return grid, oxygen_found


def run_moves(computer, grid, location, depth=1):
    counts = []
    for direction in [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]:
        grid, oxygen_found = run_move(computer, direction, grid, location, depth)
        counts.append(oxygen_found)
    return grid, min(counts)


def escape_helper(grid, location, direction, depth, history):
    next_location = get_next_square(location, direction)
    if next_location in history:
        return 0
    output = grid[next_location]

    if output == GridSpace.WALL:
        return depth
    else:
        return escape(grid, next_location, depth+1)


def escape(grid, location, depth=0, history=set()):
    history.add(location)
    counts = []
    for direction in [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]:
        count = escape_helper(grid, location, direction, depth, history)
        counts.append(count)

    return max(counts)


def main(filename='input'):
    program = open_program(filename)

    computer = IntCode(program, default_memory=8000)

    location = Point(0, 0)
    grid = defaultdict(lambda: 0)
    grid[location] = GridSpace.DROID

    grid, oxygen_location = run_moves(computer, grid, location)

    print_grid(grid)

    return oxygen_location, escape(grid, Point(-16, 14))


def print_grid(grid):
    display = {
        GridSpace.UNKNOWN: ' ',
        GridSpace.WALL: '#',
        GridSpace.EMPTY: '.',
        GridSpace.DROID: 'D',
        GridSpace.OXYGEN_SYSTEM: '*',
    }
    grid = grid.copy()
    min_x = min(point.x for point in grid.keys())
    max_x = max(point.x for point in grid.keys())
    min_y = min(point.y for point in grid.keys())
    max_y = max(point.y for point in grid.keys())

    for pos_y in range(min_y, max_y + 1):
        for pos_x in range(min_x, max_x + 1):
            print(display[grid[Point(pos_x, pos_y)]], end='')
        print('')

    print('-----------------')


if __name__ == "__main__":
    print(main())
