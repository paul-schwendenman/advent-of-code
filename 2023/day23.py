import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing

class Point(typing.NamedTuple):
    x: int
    y: int

    def get_neighbors(self):
        # for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


def print_grid(grid, path=[], start=None, end=None):
    max_x = max(point.x for point in grid.keys()) + 1
    max_y = max(point.y for point in grid.keys()) + 1
    for y in range(max_y):
        for x in range(max_x):
            if (x,y) == start:
                print('S', end='')
            elif (x,y) == end:
                print('E', end='')
            elif (x,y) in path:
                print('O', end='')
            else:
                print(grid[(x,y)], end='')
        print('')
    print('')


def part1(data):
    lines = [list(line.rstrip()) for line in list(data)]
    grid = {}
    start, end = None, None

    for y, line in enumerate(lines):
        for x, chr in enumerate(line):
            grid[Point(x, y)] = chr
            if y == 0 and chr == '.':
                start = Point(x, y)
            elif y == len(lines) - 1 and chr == '.':
                end = Point(x, y)

    queue = collections.deque([(start, 0, ())])
    distances = []

    while queue:
        location, distance, seen = queue.popleft()

        if location == end:
            distances.append(distance)
            print(f'found: {distance} left:{len(queue)} total:{len(distances)}')
            continue

        if location in seen:
            continue
        seen = seen + (location,)

        match grid.get(location):
            case '#':
                continue
            case '.':
                for neighbor in location.get_neighbors():
                    queue.append((neighbor, distance + 1, seen))
            case '>':
                queue.append((location + (1, 0), distance + 1, seen))
            case '^':
                queue.append((location + (0, -1), distance + 1, seen))
            case 'v':
                queue.append((location + (0, 1), distance + 1, seen))
            case '<':
                queue.append((location + (-1, 0), distance + 1, seen))
            case None:
                continue
            case _:
                raise ValueError("Missing tile")

    return max(distances)


def part2(data):
    lines = [list(line.rstrip()) for line in list(data)]
    grid = {}
    start, end = None, None

    for y, line in enumerate(lines):
        for x, chr in enumerate(line):
            grid[Point(x, y)] = chr
            if y == 0 and chr == '.':
                start = Point(x, y)
            elif y == len(lines) - 1 and chr == '.':
                end = Point(x, y)

    queue = collections.deque([(start, 0, ())])
    distances = []

    while queue:
        location, distance, seen = queue.popleft()

        if location == end:
            distances.append(distance)
            print(f'found: {distance} left:{len(queue)} total:{len(distances)}')
            continue

        if location in seen:
            continue
        seen = seen + (location,)

        match grid.get(location):
            case '#':
                continue
            case '.' | '>' | '<' | '^' | 'v':
                for neighbor in location.get_neighbors():
                    queue.append((neighbor, distance + 1, seen))
            case None:
                continue
            case _:
                raise ValueError("Missing tile")

    return max(distances)
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
