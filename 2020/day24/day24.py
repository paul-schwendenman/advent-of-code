from __future__ import annotations
from typing import Sequence, Mapping, MutableMapping, Tuple
from aoc import readfile, profiler
from itertools import zip_longest, islice, chain
from dataclasses import dataclass
import cProfile
from collections import namedtuple, defaultdict, deque
from enum import Enum


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def neighboors(self):
        for direction in ((-2, 0), (-1, 1), (1, 1), (2, 0), (1, -1), (-1, -1)):
            yield self + direction

    def __add__(self: Point, other: Tuple) -> Point:
        return Point(self.x + other[0], self.y + other[1])


class Direction():
    SW = Point(-1, -1)
    # S = Point(0, -2)
    SE = Point(1, -1)
    E = Point(2, 0)
    NE = Point(1, 1)
    # N = Point(0, 2)
    NW = Point(-1, 1)
    W = Point(-2, 0)


def parse_instruction(line: str) -> Point:
    cursor = 0
    tile = Point(0, 0)

    while cursor < len(line):
        if line[cursor] == 's':
            if line[cursor+1] == 'w':
                tile += Direction.SW
                cursor += 2
            elif line[cursor+1] == 'e':
                tile += Direction.SE
                cursor += 2
            else:
                raise ValueError(f'invalid cursor "{line[cursor]}" at {cursor} in {line}')
        elif line[cursor] == 'n':
            if line[cursor+1] == 'w':
                tile += Direction.NW
                cursor += 2
            elif line[cursor+1] == 'e':
                tile += Direction.NE
                cursor += 2
            else:
                raise ValueError(f'invalid cursor "{line[cursor]}" at {cursor} in {line}')
        elif line[cursor] == 'e':
            tile += Direction.E
            cursor += 1
        elif line[cursor] == 'w':
            tile += Direction.W
            cursor += 1
        else:
            raise ValueError(f'invalid cursor "{line[cursor]}" at {cursor} in {line}')

    return tile



@profiler
def part1(data: Sequence[str]) -> int:
    tiles = defaultdict(bool)

    for line in data:
        tile = parse_instruction(line)
        print(f'flipping {tile} from {tiles[tile]} to {not tiles[tile]}')
        tiles[tile] = not tiles[tile]

    return sum(tiles.values())

@profiler
def part2(data: Sequence[str]) -> int:
    tiles: MutableMapping[Point, bool] = defaultdict(bool)

    for line in data:
        tile = parse_instruction(line)
        print(f'flipping {tile} from {tiles[tile]} to {not tiles[tile]}')
        tiles[tile] = not tiles[tile]

    art: Mapping[Point, bool] = tiles.copy()

    print(f'Day 0: {sum(art.values())}')

    for day in range(100):
        new_art = {}

        for tile, color in art.items():
            black = 0

            for neighboor in tile.neighboors():
                if neighboor in art:
                    black += art[neighboor]
                else:
                    new_art[neighboor] = 2 == sum(art[neighboor2] for neighboor2 in neighboor.neighboors() if neighboor2 in art)

            if color:
                if black in (0, 3, 4, 5, 6):
                    new_art[tile] = False
                else:
                    new_art[tile] = True
            else:
                if black == 2:
                    new_art[tile] = True
                else:
                    new_art[tile] = False

        art = new_art
        print(f'Day {day+1}: {sum(new_art.values())}')

    return sum(art.values())







def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
