import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


class Point(collections.namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighbors(self):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

def make_grid(lines):
    grid = collections.defaultdict(str)
    xs = set()
    a_s = set()

    for y, line in enumerate(lines):
        for x, char in enumerate(line.rstrip()):
            grid[Point(x, y)] = char
            if char == 'X':
                xs.add(Point(x,y))
            if char == 'A':
                a_s.add(Point(x, y))



    return grid, xs, a_s

def part1(data):
    grid, xs, _ = make_grid(data)

    found = 0

    print('xs:\t', len(xs))

    for x in xs:
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
            if grid[x + offset] == 'M' and grid[x + offset + offset] == 'A' and grid[x + offset + offset + offset] == 'S':
                found += 1
                print(x, ''.join([grid[x], grid[x + offset], grid[x + offset + offset], grid[x + offset + offset + offset]]) )

    return found


    pass


def part2(data):
    grid, _, a_s = make_grid(data)

    found = 0

    print('xs:\t', len(a_s))

    for a in a_s:
        here = False
        if grid[a + (1, 1)] == 'S' and grid[a+ (-1, 1)] == 'S' and grid[a + (1, -1)] == 'M' and grid[a + (-1, -1)] == 'M':
            found += 1
            here = True
        if grid[a + (1, 1)] == 'M' and grid[a+ (-1, 1)] == 'M' and grid[a + (1, -1)] == 'S' and grid[a + (-1, -1)] == 'S':
            here = True
            found += 1
        if grid[a + (1, 1)] == 'S' and grid[a+ (-1, 1)] == 'M' and grid[a + (1, -1)] == 'S' and grid[a + (-1, -1)] == 'M':
            found += 1
            here = True
        if grid[a + (1, 1)] == 'M' and grid[a+ (-1, 1)] == 'S' and grid[a + (1, -1)] == 'M' and grid[a + (-1, -1)] == 'S':
            here = True
            found += 1
        if here:
            print(a)
            # print(''.join([grid[a + (-1, -1)], grid[a + (0, -1)], grid[a + (1, -1)]]))
            # print(''.join([grid[a + (-1, 0)], grid[a + (0, 0)], grid[a + (1, 0)]]))
            # print(''.join([grid[a + (-1, 1)], grid[a + (0, 1)], grid[a + (1, 1)]]))
            print(''.join([grid[a + (-1, -1)], ' ', grid[a + (1, -1)]]))
            print(''.join([' ', grid[a + (0, 0)], ' ']))
            print(''.join([grid[a + (-1, 1)], ' ', grid[a + (1, 1)]]))
            print('')

    return found
    # 926
    pass


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
