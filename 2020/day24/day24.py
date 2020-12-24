from __future__ import annotations
from typing import Sequence, Mapping, MutableMapping, Tuple, Generator
from aoc import readfile, profiler
from collections import namedtuple, defaultdict
from enum import Enum, auto


class Color(Enum):
    WHITE = auto()
    BLACK = auto()


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def neighboors(self) -> Generator[Point, None, None]:
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


def parse_instructions(instructions: Sequence[str]) -> Mapping[Point, Color]:
    tiles: MutableMapping[Point, Color] = defaultdict(lambda: Color.WHITE)

    for instruction in instructions:
        tile = parse_instruction(instruction)
        tiles[tile] = Color.WHITE if tiles[tile] == Color.BLACK else Color.BLACK

    return tiles


@profiler
def part1(data: Sequence[str]) -> int:
    tiles = parse_instructions(data)

    return sum(tile == Color.BLACK for tile in tiles.values())

@profiler
def part2(data: Sequence[str]) -> int:
    art = parse_instructions(data)

    for day in range(100):
        new_art = {}

        for tile, color in art.items():
            black = 0

            for neighboor in tile.neighboors():
                if neighboor in art:
                    black += (art[neighboor] == Color.BLACK)
                else:
                    new_art[neighboor] = (Color.BLACK
                                          if 2 == sum(art[neighboor2] == Color.BLACK
                                                      for neighboor2 in neighboor.neighboors()
                                                      if neighboor2 in art)
                                          else Color.WHITE)

            if color == Color.BLACK:
                if black in (0, 3, 4, 5, 6):
                    new_art[tile] = Color.WHITE
                else:
                    new_art[tile] = Color.BLACK
            else:
                if black == 2:
                    new_art[tile] = Color.BLACK
                else:
                    new_art[tile] = Color.WHITE

        art = new_art

    return sum(tile == Color.BLACK for tile in art.values())


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
