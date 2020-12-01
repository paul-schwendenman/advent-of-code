import itertools
import sys

def part1(expenses):
    pairs = itertools.permutations(expenses, 2)

    for x, y in pairs:
        if x + y == 2020:
            break

    return x * y

def part2(expenses):
    pairs = itertools.permutations(expenses, 3)

    for x, y, z in pairs:
        if x + y + z == 2020:
            break

    return x * y * z

def main(filename):
    lines = []
    with open(filename) as file:
        lines = file.readlines()

    print(part1(int(line) for line in lines))
    print(part2(int(line) for line in lines))


if __name__ == '__main__':
    main(sys.argv[1])
