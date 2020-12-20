from __future__ import annotations
from typing import Sequence, Mapping, List
from itertools import permutations, product
from functools import lru_cache, reduce
from operator import mul
from collections import defaultdict
from aoc import readfile, tracer, profiler
from dataclasses import dataclass
from math import sqrt
from enum import Enum, auto
import regex


class Rotation(Enum):
    COUNTER_CLOCKWISE = auto()
    CLOCKWISE = auto()


class Axis(Enum):
    VERTICAL = auto()
    HORIZONTAL = auto()


@dataclass
class Tile:
    tile_id: int
    shape: List[List[str]]

    def match(self, other):
        return any(side1 == side2 for side1, side2 in product(self.sides, other.sides + other.sides_reversed))

    def above(self, other):
        return self.bottom == other.top or self.bottom == other.top_reversed

    def rotate(self, rotation: Rotation):
        if rotation == Rotation.CLOCKWISE:
            self.transpose()
            self.flip(Axis.HORIZONTAL)
        else:
            self.transpose()
            self.flip(Axis.VERTICAL)

    def rotations(self):
        for _ in range(4):
            self.rotate(Rotation.CLOCKWISE)
            yield self
        self.transpose()
        for _ in range(4):
            self.rotate(Rotation.CLOCKWISE)
            yield self

    def all(self):
        pass

    def transpose(self) -> None:
        self.shape = [list(row) for row in zip(*self.shape)]

    def flip(self, axis: Axis) -> None:
        if axis == Axis.HORIZONTAL:
            self.shape = [list(reversed(row)) for row in self.shape]
        elif axis == Axis.VERTICAL:
            self.shape = list(reversed(self.shape))

    def __str__(self):
        return f'Tile {self.tile_id}:\n' + '\n'.join(''.join(row) for row in self.shape)

    @property
    def left(self):
        return ''.join(row[0] for row in self.shape)

    @property
    def right(self):
        return ''.join(row[-1] for row in self.shape)

    @property
    def top(self):
        return ''.join(self.shape[0])

    @property
    def bottom(self):
        return ''.join(self.shape[-1])

    @property
    def left_reversed(self):
        return ''.join(reversed(self.left))

    @property
    def right_reversed(self):
        return ''.join(reversed(self.right))

    @property
    def top_reversed(self):
        return ''.join(reversed(self.top))

    @property
    def bottom_reversed(self):
        return ''.join(reversed(self.bottom))

    @property
    def sides(self):
        return [
            self.left,
            self.right,
            self.top,
            self.bottom,
        ]

    @property
    def sides_reversed(self):
        return [
            self.left_reversed,
            self.right_reversed,
            self.top_reversed,
            self.bottom_reversed,
        ]


def parse_tile(tile):
    tile_id = int(tile[0].split(' ')[1][:-1])
    shape = [list(row) for row in tile[1:]]

    return Tile(tile_id, shape)


@profiler
def part1(data: Sequence[str]) -> int:
    tiles = {}
    tiles_matches = defaultdict(list)
    for raw_tile in ('\n'.join(data)).split('\n\n'):
        tile = parse_tile(raw_tile.rstrip().split('\n'))
        tiles[tile.tile_id] = tile

    for pairing in permutations(tiles.keys(), 2):
        if tiles[pairing[0]].match(tiles[pairing[1]]):
            tiles_matches[pairing[0]].append(pairing[1])

    corners = [tiles[key].tile_id for key, value in tiles_matches.items() if len(value) == 2]
    print(f'corners: {corners}')

    return reduce(mul, corners)


@profiler
def part2(data: Sequence[str]) -> int:
    tiles = {}
    tiles_matches = defaultdict(set)
    for raw_tile in ('\n'.join(data)).split('\n\n'):
        tile = parse_tile(raw_tile.rstrip().split('\n'))
        tiles[tile.tile_id] = tile

    for pairing in permutations(tiles.keys(), 2):
        if tiles[pairing[0]].match(tiles[pairing[1]]):
            tiles_matches[pairing[0]].add(pairing[1])

    neighbor_count = [(tiles[key].tile_id, len(value)) for key, value in tiles_matches.items()]
    corners = list(map(lambda a: a[0], filter(lambda a: a[1] == 2, neighbor_count)))
    number_of_tiles = len(tiles.keys())
    length_of_side = int(sqrt(number_of_tiles))


    puzzle = [[None] * length_of_side for _ in range(length_of_side)]

    puzzle[0][0] = tiles[corners[0]]

    # print(f'number of tiles: {len(tiles.keys())}')
    # print(f'corners: {corners}')
    # print(f'edges: {len(list(map(lambda a: a[0], filter(lambda a: a[1] == 3, neighbor_count))))}')

    # print(puzzle[0][0])
    # puzzle[0][0].transpose()
    # print(puzzle[0][0])

    # for piece in puzzle[0][0].rotations():
        # print(piece)


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
