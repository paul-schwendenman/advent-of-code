import fileinput
import itertools
import collections


class Point(collections.namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighbors(self):
        # for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


def find_galaxies(data, expansion=2):
    lines = [list(l.strip()) for l in data]
    galaxies: set[Point] = set()
    columns = list(map(list, zip(*lines)))
    dx, dy = 0, 0

    for y, line in enumerate(lines):
        dx = 0
        if all(map(lambda item: item == '.', line)):
            dy += expansion - 1
        for x, chr in enumerate(line):
            if all(map(lambda item: item == '.', columns[x])):
                dx += expansion - 1

            if chr == '#':
                galaxies.add(Point(x + dx, y + dy))

    return galaxies


def part1(data, expansion=2):
    galaxies = find_galaxies(data, expansion)

    galaxy_pairs: tuple(Point, Point) = itertools.combinations(galaxies, 2)

    return sum(start.manhattan(goal) for start, goal in galaxy_pairs)


def part2(data, expansion=1_000_000):
    return part1(data, expansion)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
