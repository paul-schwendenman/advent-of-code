from __future__ import annotations
from typing import Sequence, Mapping
from itertools import permutations, product
from functools import lru_cache, reduce
from operator import mul
from collections import defaultdict
from aoc import readfile, tracer, profiler
from dataclasses import dataclass
import regex


@dataclass
class Tile:
    tile_id: str
    top: str
    bottom: str
    left: str
    right: str

    def match(self, other):
        return any(side1 == side2 for side1, side2 in product(self.sides, other.sides + other.sides_reversed))

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
            ''.join(reversed(self.left)),
            ''.join(reversed(self.right)),
            ''.join(reversed(self.top)),
            ''.join(reversed(self.bottom)),
        ]


def parse_tile(tile):
    tile_id = tile[0].split(' ')[1][:-1]
    top = tile[1]
    bottom = tile[-1]
    left = ''.join(row[0] for row in tile[1:])
    right = ''.join(row[-1] for row in tile[1:])

    return Tile(tile_id, top, bottom, left, right)


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

    return reduce(mul, map(int, corners))




@profiler
def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
