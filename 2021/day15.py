import fileinput
from collections import *


def printgrid(grid, end):
    for j in range(end[1] + 1):
        print("".join(str(grid[(i, j)]) for i in range(end[0] + 1)))


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
    little_grid = {
        (x, y): int(value)
        for y, line in enumerate(lines)
        for x, value in enumerate(line)
    }
    grid = {}

    start = (0, 0)
    max_x, max_y = len(lines[0]), len(lines)

    end = (max_x * 5 - 1, max_y * 5 - 1)

    for j in range(5):
        for i in range(5):
            for location, value in little_grid.items():
                x, y = location
                # print (f'{i} * {max_x} + {x} = {i * max_x + x}, {j} * {max_y} + {y} = {j * max_y + y}')
                assert (i * max_x + x, j * max_y + y) not in grid
                new_value = value + i + j
                grid[(i * max_x + x, j * max_y + y)] = new_value if new_value <= 9 else new_value - 9

    assert end in grid
    # printgrid(grid, end)

    return find_cost(grid, start, end)


def main():
    with fileinput.input() as input:
        lines = [line.rstrip() for line in input]

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
