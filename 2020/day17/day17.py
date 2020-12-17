from __future__ import annotations
from typing import Sequence
from aoc import readfile
from dataclasses import dataclass
from collections import defaultdict, namedtuple


class Point(namedtuple('Point', 'x y z')):
    pass


class HyperPoint(namedtuple('HyperPoint', 'x y z w')):
    pass

    # def __hash__(self):
    #     return self.x * 1000000 + self.y * 1000 + self.z


def parse_grid(data):
    grid = defaultdict(str)
    for y, line in enumerate(data):
        for x, value in enumerate(line):
            grid[Point(x, y, 0)] = value

    return grid


def get_neighbors(point):
    for z in (-1, 0, 1):
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                if x == 0 and y == 0 and z == 0:
                    continue
                yield Point(x+point.x, y+point.y, z+point.z)


def print_grid(grid, max_x, max_y, max_z):
    for z in range(-max_z, max_z+1):
        print(f'level: {z}')
        for y in range(-max_y, max_y):
            for x in range(-max_x, max_x):
                print(grid[Point(x, y, z)], end='')
            print()



def part1(data: Sequence[str]) -> int:
    grid = parse_grid(data)
    max_x = len(data[0])
    max_y = len(data)
    max_z = 0
    print_grid(grid, max_x, max_y, 1)


    for cycle in range(1, 7):
        new_grid = defaultdict(str)
        for z in range(-cycle, cycle+1):
            for y in range(-cycle, max_y + cycle):
                for x in range(-cycle, max_x + cycle):
                    here = Point(x, y, z)
                    active_neighboors = len([neighboor for neighboor in get_neighbors(here) if grid[neighboor] == '#'])
                    # if z == 0 and x == 0 and y == 0:
                        # print(f'{here}: {list(get_neighbors(here))}')
                    # print(f'{here}: {list(grid[i] for i in get_neighbors(here))}')

                    if grid[here] == '#':
                        new_grid[here] = '#' if active_neighboors in (2, 3) else '.'
                    else:
                        new_grid[here] = '#' if active_neighboors == 3 else '.'
                    print(here, active_neighboors, f'{grid[here]:2s}->{new_grid[here]:2s}', active_neighboors in (2,3))
        print(f'After {cycle} cycle:')
        print_grid(new_grid, max_x+cycle, max_y+cycle, cycle)
        grid = new_grid
        print(f"active count: {sum(1 for item in grid.values() if item == '#')}")

    return sum(1 for item in grid.values() if item == '#')


def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
