from contextlib import contextmanager
import fileinput
import functools
import operator


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


def prod(*args: int) -> int:
    return functools.reduce(operator.mul, args)


def tree_count(map, slope_x, slope_y):
    count = 0
    pos_x, pos_y = 0, 0

    height = len(map)
    width = len(map[0])

    while pos_y < height:
        if (map[pos_y])[pos_x % width] == '#':
            count += 1

        pos_x += slope_x
        pos_y += slope_y

    return count


def part1(map):
    return tree_count(map, 3, 1)


def part2(map):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    trees = [tree_count(map, *slope) for slope in slopes]

    return prod(*trees)


def main(filename=None):
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
