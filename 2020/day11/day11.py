from __future__ import annotations
from typing import List, Iterator, Tuple
from collections import namedtuple, defaultdict
from enum import Enum
from aoc import readfile


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighboors(self) -> Iterator[Point]:
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)):
            yield self + offset

    def __add__(self: Point, other: Tuple) -> Point:
        return Point(self.x + other[0], self.y + other[1])


class Position(Enum):
    FLOOR = '.'
    EMPTY = 'L'
    OCCUPIED = '#'


def parse_grid(raw_grid):
    grid = defaultdict(str)

    for x_index, line in enumerate(raw_grid):
        for y_index, item in enumerate(line):
            grid[Point(x_index, y_index)] = Position(item)

    return grid


def part1(data: List[str]) -> int:
    x_max = len(data)
    y_max = len(data[0])

    grid = parse_grid(data)

    last_seat_count = 0
    seat_count = 0

    while True:
        new_grid = defaultdict(str)

        for x_index in range(x_max):
            for y_index in range(y_max):
                here = Point(x_index, y_index)
                current = grid[here]

                if current == Position.FLOOR:
                    new_grid[here] = current
                    continue

                count = sum(grid[neighboor] == Position.OCCUPIED for neighboor in here.get_neighboors())

                if count >= 4:
                    new_grid[here] = Position.EMPTY
                elif count == 0:
                    new_grid[here] = Position.OCCUPIED
                else:
                    new_grid[here] = current

        seat_count = sum(seat == Position.OCCUPIED for _, seat in new_grid.items())

        if last_seat_count == seat_count:
            break

        last_seat_count = seat_count
        grid = new_grid

    return seat_count






def part2(data: List[str]) -> int:
    x_max = len(data)
    y_max = len(data[0])

    grid = parse_grid(data)

    last_seat_count = 0
    seat_count = 0

    while True:
        new_grid = defaultdict(str)

        for x_index in range(x_max):
            for y_index in range(y_max):
                here = Point(x_index, y_index)
                current = grid[here]

                if current == Position.FLOOR:
                    new_grid[here] = Position.FLOOR
                    continue

                count = 0

                for direction in Point(0, 0).get_neighboors():
                    next_seat = here + direction
                    while grid[next_seat]:
                        if grid[next_seat] == Position.FLOOR:
                            next_seat += direction
                        elif grid[next_seat] == Position.OCCUPIED:
                            count += 1
                            break
                        elif grid[next_seat] == Position.EMPTY:
                            break

                # count = sum(grid[neighboor] == '#' for neighboor in here.get_neighboors())

                if count >= 5:
                    new_grid[here] = Position.EMPTY
                elif count == 0:
                    new_grid[here] = Position.OCCUPIED
                else:
                    new_grid[here] = current

        seat_count = sum(seat == Position.OCCUPIED for _, seat in new_grid.items())

        if last_seat_count == seat_count:
            break

        last_seat_count = seat_count
        grid = new_grid

    return seat_count


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
