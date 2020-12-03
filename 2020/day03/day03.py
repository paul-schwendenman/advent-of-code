import fileinput
import functools
import operator


def prod(*args: int) -> int:
    return functools.reduce(operator.mul, args)


def tree_count(map, slope_x, slope_y):
    count = 0
    pos_x, pos_y = 0, 0

    height = len(map)
    width = len(map[0])

    while pos_y < height:

        # print(pos_x, pos_y, map[pos_y][pos_x % (width - 1)] == '#')
        if (map[pos_y])[pos_x % (width - 1)] == '#':
            count += 1

        pos_x += slope_x
        pos_y += slope_y

    return count


def part1(map):
    count = 0
    pos_x, pos_y = 0, 0

    height = len(map)
    width = len(map[0])

    while pos_y < height:

        # print(pos_x, pos_y, map[pos_y][pos_x % (width - 1)] == '#')
        if (map[pos_y])[pos_x % (width - 1)] == '#':
            count += 1

        pos_x += 3
        pos_y += 1

    return count


def part2(map):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    trees = [tree_count(map, *slope) for slope in slopes]

    return prod(*trees)


def main():
    with fileinput.input() as data:
        lines = list(data)

    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
