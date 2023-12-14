import fileinput
import re
import itertools
import math
import functools
import collections
import enum


class Point(collections.namedtuple('Point', 'x y')):
    __slots__ = ()

    # def get_neighboors(self):
    #     for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
    #         yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])


def transpose(grid):
    return list(zip(*grid))


def part1(data):
    offset = (0, -1)
    grid = collections.defaultdict(lambda: '#')

    for j, line in enumerate(data):
        for i, space in enumerate(line.strip()):
            grid[Point(i, j)] = space
    else:
        max_x, max_y = i + 1, j + 1
    pass

    # for j in range(11):
    #     print(''.join(grid.get((i, j), ' ') for i in range(11)))

    # print(f'{max_x=} {max_y=}')

    moved = True
    while moved:
        moved = False

        for j in range(1, max_y):
            for i in range(0, max_x):
                pos = Point(i, j)

                if grid[pos] in ('.', '#'):
                    continue
                if grid[nxt := (i, j-1)] == '.':
                    moved = True
                    grid[nxt] = 'O'
                    grid[pos] = '.'
                    pass


    # for j in range(11):
    #     print(''.join(grid.get((i, j), ' ') for i in range(11)))

    return sum(max_y - y for (_, y), space in grid.items() if space == 'O' )










def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
