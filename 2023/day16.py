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
        # print(f'{energized=}')
        location, facing = queue.popleft()

        if (location, facing) in visited:
            continue

        visited.add((location, facing))

        if location in grid:
            energized.add(location)

        match grid.get(location, None), facing:
            case None, _:
                # print('hit border', location, facing)
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
    grid, _, _ = parse_grid(data)

    start = Point(3, 0)
    start_direction = Direction.DOWN
    # start = Point(0, 0)
    # start_direction = Direction.RIGHT

    energized = track_beams(grid, start, start_direction)

    return len(energized)


def part2(data):
    grid, max_x, max_y = parse_grid(data)
    energized_map = {}

    left_row = ((Point(0, y), Direction.RIGHT) for y in range(max_y + 1))
    right_row = ((Point(max_x, y), Direction.LEFT) for y in range(max_y + 1))
    top_row = ((Point(x, 0), Direction.DOWN) for x in range(max_x + 1))
    bottom_row = ((Point(x, max_y), Direction.UP) for x in range(max_x + 1))

    # for start_location, start_direction in itertools.chain(top_row):
    for start_location, start_direction in itertools.chain(top_row, bottom_row, left_row, right_row):
        # print(f'{start_location=} {start_direction=}')
        energized = track_beams(grid, start_location, start_direction)

        energized_map[(start_location, start_direction)] = energized

    # pprint.pprint({key: len(value) for key, value in energized_map.items()})
    # pprint.pprint({key: (value) for key, value in energized_map.items()})

    return max(len(a) for a in energized_map.values())
    # return max((len(a | b), a, b) for a, b in itertools.combinations(energized_map.values(), 2))
    top = max((len(a[1] | b[1]), a, b) for a, b in itertools.combinations(energized_map.items(), 2))

    print(top[1][0], top[2][0],)
    show_energized(grid, top[1][1] | top[2][1])

    return len(top[1][1] | top[2][1])


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
