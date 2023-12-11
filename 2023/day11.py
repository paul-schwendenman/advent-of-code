import fileinput
import re
import itertools
import math
import functools
import collections
import enum
from heapq import heapify, heappop, heappush
from tqdm import tqdm


class Space(enum.Enum):
    EMPTY = '.'
    GALAXY = '#'


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


def find_path(grid: Point, start: Point, goal, distances: dict[Point, dict[Point, int]]):
    queue = [(0, start)]
    heapify(queue)
    low = math.inf
    seen = set()

    while len(queue) > 0:
        # print(f'size={len(queue)}')
        steps, current = heappop(queue)

        if steps > low:
            continue

        if current in seen:
            continue

        seen.add(current)
        distances[start][current] = steps


        if current == goal:
            low = steps
            continue

        for neighbor in current.get_neighbors():
            heappush(queue, (steps + 1, neighbor))

    return low, distances



def parse_grid(data):
    lines = [list(l.strip()) for l in data]
    grid = collections.defaultdict(lambda: Space.EMPTY)
    galaxies = set()
    columns = list(map(list, zip(*lines)))
    dx, dy = 0, 0

    for y, line in enumerate(lines):
        dx = 0
        if all(map(lambda item: item == '.', line)):
            dy += 1
        for x, chr in enumerate(line):
            if all(map(lambda item: item == '.', columns[x])):
                # print(f'{x=}: {columns[x]=}')
                dx += 1
            location = Point(x + dx, y + dy)
            # location = Point(x, y)
            grid[location] = Space(chr)

            if chr == '#':
                galaxies.add(location)

    print(f'{x=} {y=} {dx=} {dy=}')

    return grid, galaxies


def part1(data):

    grid, galaxies = parse_grid(data)

    # for r in range(15):
        # print(''.join('.' if (grid[(c, r)]) == Space.EMPTY else "#" for c in range(15)))

    print(f'galaxies={len(galaxies)}')

    pairs: tuple(Point, Point) = itertools.combinations(galaxies, 2)
    distances: dict[Point, dict[Point, int]] = collections.defaultdict(dict)


    acc = 0

    for start, goal in tqdm(list(pairs)):
        # low, distances = find_path(grid, start, goal, distances)
        low = start.manhattan(goal)

        acc += low

    print(f'{start=} {goal=} {low=}')

    return acc
    pass

def part2(data):
    pass

def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
