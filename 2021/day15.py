import fileinput
from collections import *


def neighboors(location):
    x, y = location

    for dx in (1, -1):
        yield (x + dx, y)
    for dy in (-1, 1):
        yield (x, y + dy)


def find_cost(grid, start, goal):
    checklist = [(0, start)]

    costs = {}
    cost = None

    while True:
        cost, location = checklist[0]

        if location == goal:
            return cost

        checklist = checklist[1:]

        for neighboor in neighboors(location):
            if neighboor not in grid:
                continue

            new_cost = cost + grid[neighboor]

            if neighboor in costs and costs[neighboor] <= new_cost:
                continue

            costs[neighboor] = new_cost
            checklist.append((new_cost, neighboor))

        checklist = sorted(checklist)


def part1(lines):
    grid = {
        (x, y): int(value)
        for y, line in enumerate(lines)
        for x, value in enumerate(line)
    }

    start = (0, 0)
    end = (len(lines[0]) - 1, len(lines) - 1)

    return find_cost(grid, start, end)


def part2(lines):
    pass


def main():
    with fileinput.input() as input:
        lines = [line.rstrip() for line in input]

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
