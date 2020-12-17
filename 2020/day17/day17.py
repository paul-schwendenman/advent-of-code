from __future__ import annotations
from typing import DefaultDict, Iterator, Sequence
from aoc import readfile
from collections import defaultdict, namedtuple


class Point(namedtuple('Point', 'x y z')):
    pass


Grid = DefaultDict[Point, str]


def parse_grid(data: Sequence[str]) -> Grid:
    grid = defaultdict(lambda: '.')
    for y, line in enumerate(data):
        for x, value in enumerate(line):
            grid[Point(x, y, 0)] = value

    return grid


def get_neighbors(point: Point) -> Iterator[Point]:
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                yield Point(dx+point.x, dy+point.y, dz+point.z)


def print_grid(grid: Grid, max_x: int, max_y: int, cycle: int) -> None:
    for z in range(-cycle, cycle+1):
        print(f'level: {z}')
        for y in range(-cycle, max_y+cycle):
            for x in range(-cycle, max_x+cycle):
                print(grid[Point(x, y, z)], end='')
            print()


def part1(data: Sequence[str]) -> int:
    grid = parse_grid(data)
    initial_x = len(data[0])
    initial_y = len(data)
    initial_z = 1
    # print_grid(grid, initial_x, initial_y, 0)

    for cycle in range(1, 7):
        new_grid = defaultdict(lambda: '.')
        for z in range(-cycle, cycle+initial_z):
            for y in range(-cycle, initial_y + cycle):
                for x in range(-cycle, initial_x + cycle):
                    here = Point(x, y, z)
                    active_neighboors = sum(1 for neighboor in get_neighbors(here) if grid[neighboor] == '#')

                    if grid[here] == '#' and active_neighboors in (2, 3):
                        new_grid[here] = '#'
                    elif active_neighboors == 3:
                        new_grid[here] = '#'
        # print_grid(new_grid, initial_x, initial_y, cycle)
        grid = new_grid

    return sum(1 for item in grid.values() if item == '#')


def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
