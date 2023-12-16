import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint


class Point(collections.namedtuple('Point', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


class Direction(tuple, enum.Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


# ---- / ------
FORWARD_SLASH = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.UP,
    Direction.LEFT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
}

# ---- \ ------
BACKSLASH = {
    Direction.UP: Direction.LEFT,
    Direction.RIGHT: Direction.DOWN,
    Direction.LEFT: Direction.UP,
    Direction.DOWN: Direction.RIGHT,
}


def parse_grid(data):
    grid = {}

    for j, line in enumerate(data):
        for i, char in enumerate(line.rstrip()):
            here = Point(i, j)

            grid[here] = char

    return grid, i, j


def show_energized(grid, energized):
    for j in range(10):
        for i in range(10):
            if (i, j) in energized:
                print('#', end="")
            else:
                print(grid[(i,j)], end='')

        print('')
    print('')


def track_beams(grid, start_location, start_direction):
    energized = set()
    visited = set()

    queue = collections.deque([(start_location, start_direction)])

    while len(queue) > 0:
        location, facing = queue.popleft()

        if (location, facing) in visited:
            continue

        visited.add((location, facing))

        if location in grid:
            energized.add(location)
        else:
            continue

        match grid[location], facing:
            case '.', _:
                queue.append((location + facing, facing))
            case '/', _:
                facing = FORWARD_SLASH[facing]
                next_location = location + facing
                queue.append((next_location, facing))
                queue.append((location + facing, facing))
            case '\\', _:
                facing = BACKSLASH[facing]
                queue.append((location + facing, facing))
            case '-', Direction.RIGHT | Direction.LEFT:
                queue.append((location + facing, facing))
            case '-', Direction.UP | Direction.DOWN:
                facing = Direction.LEFT
                queue.append((location + facing, facing))
                facing = Direction.RIGHT
                queue.append((location + facing, facing))
            case '|', Direction.UP | Direction.DOWN:
                queue.append((location + facing, facing))
            case '|', Direction.RIGHT | Direction.LEFT:
                facing = Direction.UP
                queue.append((location + facing, facing))
                facing = Direction.DOWN
                queue.append((location + facing, facing))
            case symbol, direction:
                raise ValueError("No match", symbol, direction)
    return energized


def part1(data):
    grid, _, _ = parse_grid(data)

    start = Point(0, 0)
    start_direction = Direction.RIGHT

    energized = track_beams(grid, start, start_direction)

    return len(energized)


def part2(data):
    grid, max_x, max_y = parse_grid(data)
    energized_map = {}

    left_row = ((Point(0, y), Direction.RIGHT) for y in range(max_y + 1))
    right_row = ((Point(max_x, y), Direction.LEFT) for y in range(max_y + 1))
    top_row = ((Point(x, 0), Direction.DOWN) for x in range(max_x + 1))
    bottom_row = ((Point(x, max_y), Direction.UP) for x in range(max_x + 1))

    for start_location, start_direction in itertools.chain(top_row, bottom_row, left_row, right_row):
        energized = track_beams(grid, start_location, start_direction)

        energized_map[(start_location, start_direction)] = energized

    return max(len(a) for a in energized_map.values())


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
