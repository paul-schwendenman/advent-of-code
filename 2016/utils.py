from collections.abc import Iterable
from collections import defaultdict, namedtuple
from enum import Enum
from math import log10
from re import findall
from typing import TextIO, Dict
from itertools import islice


def extract_ints(string: str) -> list[int]:
    return list(map(int, findall(r'-?\d+', string)))


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


def concat_ints(x: int, y: int) -> int:
    return x * (10 ** (int(log10(y)) + 1)) + y  # int(str(x) + str(y))


class Offset(tuple, Enum):
    TOP_LEFT = (-1, -1)
    UP = (0, -1)
    NORTH = (0, -1)
    TOP_CENTER = (-1, 0)
    TOP_RIGHT = (-1, 1)
    LEFT = (-1, 0)
    WEST = (-1, 0)
    CENTER_LEFT = (0, -1)
    CENTER_CENTER = (0, 0)
    RIGHT = (1, 0)
    EAST = (1, 0)
    CENTER_RIGHT = (0, 1)
    BOTTOM_LEFT = (1, -1)
    DOWN = (0, 1)
    SOUTH = (0, 1)
    BOTTOM_CENTER = (1, 0)
    BOTTOM_RIGHT = (1, 1)

    def __getitem__(self, index):
        return self.value[index]

    def __eq__(self, tuple):
        return len(tuple) == 2 and self.value[0] == tuple[0] and self.value[1] == tuple[1]

    def __len__(self):
        return 2

    def rotate(self, clockwise=True):
        x, y = self.value

        return Offset(y, -x) if clockwise else Offset(-y, x)

    @classmethod
    def cardinal(cls):
        return (cls.UP, cls.LEFT, cls.RIGHT, cls.DOWN)

    @classmethod
    def diagonal(cls):
        return (cls.TOP_LEFT, cls.TOP_RIGHT, cls.BOTTOM_LEFT, cls.BOTTOM_RIGHT)

    @classmethod
    def all(cls):
        return cls.cardinal() + cls.diagonal()


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

    def __sub__(self, other):
        return Point(self.x - other[0], self.y - other[1])

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def get_neighbors(self, *, offsets=Offset.all()):
        for offset in offsets:
            yield self + offset


def parse_grid(data: TextIO, *, exclude=''):
    grid: Dict[Point, str] = {}
    markers: Dict[str, list[Point]] = defaultdict(list)

    for j, line in enumerate(data):
        for i, char in enumerate(line.rstrip()):
            here = Point(i, j)

            grid[here] = char

            if char not in exclude:
                markers[char].append(here)

    return grid, i, j, markers


def batched(iterable, n, *, strict=False):
    '''Batch data from the iterable into tuples of length n. The last batch may be shorter than n.

    >>> flattened_data = ['roses', 'red', 'violets', 'blue', 'sugar', 'sweet']
    >>> unflattened = list(batched(flattened_data, 2))
    >>> unflattened
    [('roses', 'red'), ('violets', 'blue'), ('sugar', 'sweet')]
    '''
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch
