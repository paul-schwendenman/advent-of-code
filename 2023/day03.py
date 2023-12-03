import fileinput
import re
from collections import defaultdict, namedtuple
from itertools import count
from math import prod


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighbors(self):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])


def part1(data):
    grid = defaultdict(str)
    symbols: list[Point] = []
    lines = list(data)

    for y, line in enumerate(lines):
        for x, space in enumerate(line.strip()):
            loc = Point(x, y)
            grid[loc] = space

            if space == '.' or space.isdigit():
                pass
            else:
                symbols.append(loc)

    acc = 0

    for symbol in symbols:
        labels = set()
        for neighbor in (neighbors := symbol.get_neighbors()):
            if grid[neighbor].isdigit():
                for j in count(neighbor.x):
                    if not grid.get((j, neighbor.y), '').isdigit():
                        break

                slice = lines[neighbor.y][:j]

                num = int(re.match(r'(?:.*[^0-9]+){0,1}(\d+)$', slice).groups()[0])

                labels.add(num)

        acc += sum(labels)

    return acc


def part2(data):
    grid = defaultdict(str)
    symbols: list[Point] = []
    lines = list(data)

    for y, line in enumerate(lines):
        for x, space in enumerate(line.strip()):
            loc = Point(x, y)
            grid[loc] = space

            if space == '.' or space.isdigit():
                pass
            else:
                symbols.append(loc)

    acc = 0

    for symbol in symbols:
        if grid[symbol] != '*':
            continue
        labels = set()
        for neighbor in (neighbors := symbol.get_neighbors()):
            if grid[neighbor].isdigit():
                for j in count(neighbor.x):
                    if not grid.get((j, neighbor.y), '').isdigit():
                        break

                slice = lines[neighbor.y][:j]
                num = int(re.match(r'(?:.*[^0-9]+){0,1}(\d+)$', slice).groups()[0])

                labels.add(num)

        if len(labels) == 2:
            acc += prod(labels)

    return acc


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
