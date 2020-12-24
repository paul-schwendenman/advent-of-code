from __future__ import annotations
from typing import Sequence, Mapping, Tuple
from aoc import readfile, profiler
from itertools import zip_longest, islice, chain
from dataclasses import dataclass
import cProfile
from collections import namedtuple, defaultdict
from enum import Enum


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

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


def parse_instruction(line):
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
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
