import fileinput
import re
import itertools
import math
import functools
import collections
import enum


class Point(collections.namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighbors(self):
        # for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            yield self + offset

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


def parse_grid(data):
    grid = {}

    for j, line in enumerate(data):
        for i, char in enumerate(line.rstrip()):
            here = Point(i, j)

            grid[here] = char

    return grid


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
        # print(f'{energized=}')
        location, facing = queue.popleft()

        if (location, facing) in visited:
            continue

        visited.add((location, facing))
        if location in grid:
            energized.add(location)

        match grid.get(location, None), facing:
            case None, _:
                continue
            case '.', _:
                next_location = location + facing
                queue.append((next_location, facing))
            case '/', Direction.RIGHT:
                facing = Direction.UP
                next_location = location + facing
                queue.append((next_location, facing))
            case '/', Direction.DOWN:
                facing = Direction.LEFT
                next_location = location + facing
                queue.append((next_location, facing))
            case '/', Direction.LEFT:
                facing = Direction.DOWN
                next_location = location + facing
                queue.append((next_location, facing))
            case '/', Direction.UP:
                facing = Direction.RIGHT
                next_location = location + facing
                queue.append((next_location, facing))
            case '\\', Direction.RIGHT:
                facing = Direction.DOWN
                next_location = location + facing
                queue.append((next_location, facing))
            case '\\', Direction.DOWN:
                facing = Direction.RIGHT
                next_location = location + facing
                queue.append((next_location, facing))
            case '\\', Direction.LEFT:
                facing = Direction.UP
                next_location = location + facing
                queue.append((next_location, facing))
            case '\\', Direction.UP:
                facing = Direction.LEFT
                next_location = location + facing
                queue.append((next_location, facing))
            case '-', Direction.RIGHT | Direction.LEFT:
                next_location = location + facing
                queue.append((next_location, facing))
            case '-', Direction.UP | Direction.DOWN:
                facing = Direction.LEFT
                next_location = location + facing
                queue.append((next_location, facing))
                facing = Direction.RIGHT
                next_location = location + facing
                queue.append((next_location, facing))
            case '|', Direction.UP | Direction.DOWN:
                next_location = location + facing
                queue.append((next_location, facing))
            case '|', Direction.RIGHT | Direction.LEFT:
                facing = Direction.UP
                next_location = location + facing
                queue.append((next_location, facing))
                facing = Direction.DOWN
                next_location = location + facing
                queue.append((next_location, facing))
            case symbol, direction:
                raise ValueError("No match", symbol, direction)
        # show_energized(grid, energized)
    return energized


def part1(data):
    grid = parse_grid(data)

    start = Point(0, 0)
    start_direction = Direction.RIGHT

    energized = track_beams(grid, start, start_direction)

    return len(energized)


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
