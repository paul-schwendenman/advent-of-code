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

    def exactly_above(self, other):
        return any(self.bottom == side for side in other.sides)

    def exactly_below(self, other):
        return any(self.top == side for side in other.sides)

    def exactly_left_of(self, other):
        return any(self.right == side for side in other.sides)

    def exactly_right_of(self, other):
        return any(self.left == side for side in other.sides)

    def above(self, other):
        return any(self.bottom == side for side in other.sides + other.sides_reversed)

    def below(self, other):
        return any(self.top == side for side in other.sides + other.sides_reversed)

    def left_of(self, other):
        return any(self.right == side for side in other.sides + other.sides_reversed)

    def right_of(self, other):
        return any(self.left == side for side in other.sides + other.sides_reversed)

    def rotate(self, rotation: Rotation) -> None:
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

    def core(self):
        return [row[1:-1] for row in self.shape[1:-1]]

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


def parse_tile(tile: List[str]) -> Tile:
    tile_id = int(tile[0].split(' ')[1][:-1])
    shape = [list(row) for row in tile[1:]]

    return Tile(tile_id, shape)


def print_puzzle_ids(puzzle: List[List[Tile]]) -> None:
    for row in puzzle:
        print(' '.join(str(tile.tile_id) if tile else '????' for tile in row))


def print_puzzle(puzzle: List[List[Tile]]) -> None:
    print('Puzzle')
    sub_row_count = len(puzzle[0][0].shape)
    for row in puzzle:
        for sub_row in range(sub_row_count):
            print('|'.join(''.join(tile.shape[sub_row] if tile else ' ' * sub_row_count) for tile in row))
        print('|'.join('-' * sub_row_count for _ in range(len(row))))


def assemble_puzzle(puzzle: List[List[Tile]]) -> List[str]:
    solution = []
    sub_row_count = len(puzzle[0][0].core())
    for row in puzzle:
        for sub_row in range(sub_row_count):
            solution.append(''.join(''.join(tile.core()[sub_row] if tile else ' ' * sub_row_count) for tile in row))

    return solution


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

    puzzle: List[List[Tile]] = [[None] * length_of_side for _ in range(length_of_side)]

    puzzle[0][0] = tiles[corners[0]]

    right_side, below = map(tiles.get, tiles_matches[corners[0]])

    print(puzzle[0][0])
    print(right_side)
    print(below)

    for index, orientation in enumerate(puzzle[0][0].rotations()):
        print(f"{index}. turning...")
        if orientation.left_of(right_side) and orientation.above(below):
            print("found rotation:")
            print(orientation)
            break
    else:
        raise Exception("No rotation found")

    # print(f'number of tiles: {len(tiles.keys())}')
    # print(f'corners: {corners}')
    # print(f'edges: {len(list(map(lambda a: a[0], filter(lambda a: a[1] == 3, neighbor_count))))}')

    print(puzzle[0][0])
    # puzzle[0][0].transpose()
    # print(puzzle[0][0])

    # for piece in puzzle[0][0].rotations():
        # print(piece)

    for row in range(length_of_side):
        for column in range(length_of_side):
            print(f'placing {row} {column}')
            if row == 0 and column == 0:
                continue
            if row == 0:
                previous = puzzle[row][column-1]
                if column == 1:
                    print(right_side)
                    options = [right_side]
                else:
                    options = map(tiles.get, tiles_matches[previous.tile_id])
                for option in options:
                    if previous.left_of(option):
                        for index, orientation in enumerate(option.rotations()):
                            print(f"{index}. turning...")
                            if orientation.exactly_right_of(previous):
                                break
                        else:
                            raise Exception("No rotation found")
                        print(f'found {option.tile_id}')
                        puzzle[row][column] = option
                        break
                    else:
                        print(f'skipping {option.tile_id}')
                else:
                    raise Exception("No option found")
            else:
                previous = puzzle[row-1][column]
                for option in map(tiles.get, tiles_matches[previous.tile_id]):
                    if previous.above(option):
                        for index, orientation in enumerate(option.rotations()):
                            print(f"{index}. turning...")
                            if orientation.below(previous):
                                break
                        else:
                            raise Exception("No rotation found")
                        print(f'found {option.tile_id}')
                        puzzle[row][column] = option
                        break
                    else:
                        print(f'skipping {option.tile_id}')
                else:
                    # print(puzzle[0][1].top)
                    # print(puzzle[0][1].bottom)
                    # print(tiles[1427])
                    print_puzzle(puzzle)
                    print_puzzle_ids(puzzle)
                    raise Exception("No option found")
    # print_puzzle(puzzle)
    print_puzzle_ids(puzzle)

    assembled = assemble_puzzle(puzzle)
    print('\n'.join(assembled))

    og_monster = ['                  # ',
                  '#    ##    ##    ###',
                  ' #  #  #  #  #  #   ']

    monster_count = 0

    print('finding monsters')
    for index, monster_tile in enumerate(Tile('monster', og_monster).rotations()):
        print(f'try {index}')
        monster = monster_tile.shape
        for base_row in range(len(assembled) - len(monster)):
            for base_column in range(len(assembled[0]) - len(monster[0])):
                if base_row == 1 and base_column == 2:
                    print('\n'.join([''.join([
                    assembled[base_row + row][base_column + column] if monster[row][column] == '#' else ' '
                    for column in range(len(monster[0]))])
                    for row in range(len(monster))]))
                if all(monster[row][column] == ' ' or
                    assembled[base_row + row][base_column + column] == '#'
                    for row in range(len(monster))
                    for column in range(len(monster[0]))):
                    monster_count += 1
    print(f'monsters: {monster_count}')

    print(''.join(assembled).count('#'))
    print(''.join(og_monster).count('#'))
    return ''.join(assembled).count('#') - (''.join(og_monster).count('#') * monster_count)






def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
