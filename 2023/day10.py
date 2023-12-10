import fileinput
import re
import itertools
import math
import functools
import collections
import enum


class Point(collections.namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighboors(self):
        # for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])


class Direction(enum.Enum):
    NORTH = enum.auto()
    SOUTH = enum.auto()
    EAST = enum.auto()
    WEST = enum.auto()

dirs = {
    Direction.NORTH: (0, -1),
    Direction.SOUTH: (0, 1),
    Direction.EAST: (1, 0),
    Direction.WEST: (-1, 0),
}

class Pipe(enum.Enum):
    '''
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    '''
    VERTICAL = '|'
    HORIZONTAL = '-'
    NORTH_EAST = 'L'
    NORTH_WEST = "J"
    SOUTH_WEST = "7"
    SOUTH_EAST = "F"
    GROUND = '.'
    START = 'S'

dir_maps = {
    Pipe.VERTICAL: [Direction.NORTH, Direction.SOUTH],
    Pipe.HORIZONTAL: (Direction.EAST, Direction.WEST),
    Pipe.NORTH_EAST: (Direction.NORTH, Direction.EAST),
    Pipe.NORTH_WEST: (Direction.NORTH, Direction.WEST),
    Pipe.SOUTH_EAST: (Direction.SOUTH, Direction.EAST),
    Pipe.SOUTH_WEST: (Direction.SOUTH, Direction.WEST),
    Pipe.GROUND: (),
    Pipe.START: (),
}


def next_pipe(location, pipe, facing):
    match pipe, facing:
        case '|', '':
            pass

def build_map(data):

    grid = {}
    start = None
    for r, line in enumerate(data):
        for c, chr in enumerate(line.strip()):
            grid[here := Point(c, r)] = Pipe(chr)

            if chr == 'S':
                start = here

    return grid, start


def find_connected(grid: dict[Point, Pipe]):
    adj = {}
    for location, pipe in (grid.items()):
        moves = [dirs[direction] for direction in dir_maps[pipe]]
        neighbors = [location + move for move in moves]

        valid = [neighbor for neighbor in neighbors if neighbor in grid]

        adj[location] = valid

    return adj




def walk_path(grid, start):
    location = start
    path = []

    while True:
        current_pipe = grid[location]

        moves = [dirs[direction] for direction in dir_maps[current_pipe]]
        next_locations = [n := (location + move) for move in moves if n not in path]

        assert len(moves) == 1

        path.append(location)
        location = location + moves[0]

        if location == start:
            break

    return path
    pass


def part1(data):
    grid, start = build_map(data)

    adjacent = find_connected(grid)

    for space, neighbors in adjacent.items():
        if start in neighbors:
            adjacent[start].append(space)

    distance = {
        start: 0
    }
    queue = collections.deque([start])

    ans = (0, start)

    while len(queue) > 0:
        current = queue.popleft()
        current_distance = distance[current]

        for nxt in adjacent[current]:

            if nxt not in distance:
                distance[nxt] = current_distance + 1
                ans = max(ans, (current_distance + 1, nxt))
                queue.append(nxt)


    return ans[0]


def part2(data):
    lines = [list(line.strip()) for line in list(data)]
    # lines[1][1] = 'F'
    grid = {}

    max_y = len(lines) * 3
    max_x = len(lines[0]) * 3

    for y in range(max_y):
        for x in range(max_x):
            grid[Point(x, y)] = '.'

    for j, line in enumerate(lines):
        for k, space in enumerate(line):
            if space == '|':
                grid[Point(3 * k + 1, 3 * j + 0)] = '#'
                grid[Point(3 * k + 1, 3 * j + 1)] = '#'
                grid[Point(3 * k + 1, 3 * j + 2)] = '#'
            elif space == "-":
                grid[Point(3 * k + 0, 3 * j + 1)] = '#'
                grid[Point(3 * k + 1, 3 * j + 1)] = '#'
                grid[Point(3 * k + 2, 3 * j + 1)] = '#'
            elif space == "L":
                grid[Point(3 * k + 1, 3 * j + 0)] = '#'
                grid[Point(3 * k + 1, 3 * j + 1)] = '#'
                grid[Point(3 * k + 2, 3 * j + 1)] = '#'
            elif space == "J":
                grid[Point(3 * k + 1, 3 * j + 0)] = '#'
                grid[Point(3 * k + 1, 3 * j + 1)] = '#'
                grid[Point(3 * k + 0, 3 * j + 1)] = '#'
            elif space == "F":
                grid[Point(3 * k + 1, 3 * j + 1)] = '#'
                grid[Point(3 * k + 1, 3 * j + 2)] = '#'
                grid[Point(3 * k + 2, 3 * j + 1)] = '#'
            elif space == "7":
                grid[Point(3 * k + 0, 3 * j + 1)] = '#'
                grid[Point(3 * k + 1, 3 * j + 1)] = '#'
                grid[Point(3 * k + 1, 3 * j + 2)] = '#'
            pass
    pass

    for y in range(max_y):
        for x in range(max_x):
            print(grid[(x, y)], end='')
        print('')

def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
