from __future__ import annotations
from typing import Sequence, List, Optional, Generator, Iterable, TypeVar, cast, MutableMapping
from itertools import permutations, product
from functools import reduce
from operator import mul
from collections import defaultdict
from aoc import readfile, profiler
from dataclasses import dataclass
from math import sqrt
from enum import Enum, auto


class Rotation(Enum):
    COUNTER_CLOCKWISE = auto()
    CLOCKWISE = auto()


class Axis(Enum):
    VERTICAL = auto()
    HORIZONTAL = auto()


T = TypeVar('T', bound='Grid')


class Grid:
    def __init__(self, grid: List[List[str]]):
        self.shape = grid

    def rotate(self, rotation: Rotation) -> None:
        if rotation == Rotation.CLOCKWISE:
            self.transpose()
            self.flip(Axis.HORIZONTAL)
        else:
            self.transpose()
            self.flip(Axis.VERTICAL)

    def rotations(self: T) -> Generator[T, None, None]:
        for _ in range(4):
            self.rotate(Rotation.CLOCKWISE)
            yield self
        self.transpose()
        for _ in range(4):
            self.rotate(Rotation.CLOCKWISE)
            yield self

    def core(self) -> List[List[str]]:
        return [row[1:-1] for row in self.shape[1:-1]]

    def transpose(self) -> None:
        self.shape = [list(row) for row in zip(*self.shape)]

    def flip(self, axis: Axis) -> None:
        if axis == Axis.HORIZONTAL:
            self.shape = [list(reversed(row)) for row in self.shape]
        elif axis == Axis.VERTICAL:
            self.shape = list(reversed(self.shape))


class Monster(Grid):
    def __init__(self, grid: List[str]):
        self.shape = [list(line) for line in grid]


@dataclass
class Tile(Grid):
    tile_id: int
    shape: List[List[str]]

    def match(self, other: Tile) -> bool:
        return any(side1 == side2 for side1, side2 in product(self.sides, other.sides + other.sides_reversed))

    def exactly_above(self, other: Tile) -> bool:
        return any(self.bottom == side for side in other.sides)

    def exactly_below(self, other: Tile) -> bool:
        return any(self.top == side for side in other.sides)

    def exactly_left_of(self, other: Tile) -> bool:
        return any(self.right == side for side in other.sides)

    def exactly_right_of(self, other: Tile) -> bool:
        return any(self.left == side for side in other.sides)

    def above(self, other: Tile) -> bool:
        return any(self.bottom == side for side in other.sides + other.sides_reversed)

    def below(self, other: Tile) -> bool:
        return any(self.top == side for side in other.sides + other.sides_reversed)

    def left_of(self, other: Tile) -> bool:
        return any(self.right == side for side in other.sides + other.sides_reversed)

    def right_of(self, other: Tile) -> bool:
        return any(self.left == side for side in other.sides + other.sides_reversed)

    def core(self) -> List[List[str]]:
        return [row[1:-1] for row in self.shape[1:-1]]

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


PartialPuzzle = List[List[Optional[Tile]]]
Puzzle = List[List[Tile]]


def parse_tile(tile: List[str]) -> Tile:
    tile_id = int(tile[0].split(' ')[1][:-1])
    shape = [list(row) for row in tile[1:]]

    return Tile(tile_id, shape)


def print_puzzle_ids(puzzle: PartialPuzzle) -> None:
    for row in puzzle:
        print(' '.join(str(tile.tile_id) if tile else '????' for tile in row))


def print_puzzle(puzzle: PartialPuzzle) -> None:
    print('Puzzle')
    sub_row_count = len(puzzle[0][0].shape) if puzzle[0][0] is not None else 0
    for row in puzzle:
        for sub_row in range(sub_row_count):
            print('|'.join(''.join(tile.shape[sub_row] if tile else ' ' * sub_row_count) for tile in row))
        print('|'.join('-' * sub_row_count for _ in range(len(row))))


def assemble_puzzle(puzzle: Puzzle) -> List[str]:
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

    return reduce(mul, corners)


@profiler
def part2(data: Sequence[str]) -> int:
    tiles: MutableMapping[int, Tile] = {}
    tiles_matches = defaultdict(set)
    for raw_tile in ('\n'.join(data)).split('\n\n'):
        tile = parse_tile(raw_tile.rstrip().split('\n'))
        tiles[tile.tile_id] = tile

    for pairing in permutations(tiles.keys(), 2):
        if tiles[pairing[0]].match(tiles[pairing[1]]):
            tiles_matches[pairing[0]].add(pairing[1])

    neighbor_count = [(tiles[key].tile_id, len(value)) for key, value in tiles_matches.items()]
    corners = list(map(lambda b: b[0], filter(lambda a: a[1] == 2, neighbor_count)))
    number_of_tiles = len(tiles.keys())
    length_of_side = int(sqrt(number_of_tiles))

    puzzle: PartialPuzzle = [[None] * length_of_side for _ in range(length_of_side)]

    right_side, below = map(tiles.__getitem__, tiles_matches[corners[0]])

    first_tile = tiles[corners[0]]
    puzzle[0][0] = first_tile

    for index, orientation in enumerate(first_tile.rotations()):
        if orientation.left_of(right_side) and orientation.above(below):
            break
    else:
        raise Exception("No rotation found")

    for row in range(length_of_side):
        for column in range(length_of_side):
            if row == 0 and column == 0:
                continue
            if row == 0:
                options: Iterable[Tile]
                previous = puzzle[row][column-1]
                if previous is None:
                    raise ValueError("Previous tile not positioned")
                if column == 1:
                    options = [right_side]
                else:
                    options = map(tiles.__getitem__, tiles_matches[previous.tile_id])
                for option in options:
                    if previous.left_of(option):
                        for index, orientation in enumerate(option.rotations()):
                            if orientation.exactly_right_of(previous):
                                break
                        else:
                            raise Exception("No rotation found")
                        puzzle[row][column] = option
                        break
                else:
                    raise Exception("No option found")
            else:
                previous = puzzle[row-1][column]
                if previous is None:
                    raise ValueError("Previous tile not positioned")
                for option in map(tiles.__getitem__, tiles_matches[previous.tile_id]):
                    if previous.above(option):
                        for index, orientation in enumerate(option.rotations()):
                            if orientation.exactly_below(previous):
                                break
                        else:
                            raise Exception("No rotation found")
                        puzzle[row][column] = option
                        break
                else:
                    print_puzzle(puzzle)
                    print_puzzle_ids(puzzle)
                    raise Exception("No option found")

    assembled = assemble_puzzle(cast(Puzzle, puzzle))

    og_monster = ['                  # ',
                  '#    ##    ##    ###',
                  ' #  #  #  #  #  #   ']

    monster_count = 0

    for monster_tile in Monster(og_monster).rotations():
        monster = monster_tile.shape
        for base_row in range(len(assembled) - len(monster)):
            for base_column in range(len(assembled[0]) - len(monster[0])):
                if all(monster[row][column] == ' ' or
                       assembled[base_row + row][base_column + column] == '#'
                       for row in range(len(monster))
                       for column in range(len(monster[0]))):
                    monster_count += 1
    return ''.join(assembled).count('#') - (''.join(og_monster).count('#') * monster_count)


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
