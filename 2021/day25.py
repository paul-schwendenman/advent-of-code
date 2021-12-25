import fileinput
from itertools import cycle, product, count
from collections import Counter, namedtuple
from typing import MutableMapping, Tuple
from enum import Enum

def print_grid(grid, max_x, max_y):
    for j in range(0, max_y):
        print("".join(grid.get((i, j), '.') for i in range(0, max_x)))

def next_location(current, max):
    if current + 1 < max:
        return current + 1

    return 0


def part1(data: list[str]) -> int:
    grid = {}
    max_x = len(data[0])
    max_y = len(data)

    for j, line in enumerate(data):
        for i, space in enumerate(line):
            grid[(i, j)] = space

    for step in count(1):
        # print('------------------------')
        if step % 100 == 0:
            print(f'step {step}')
        # print_grid(grid, max_x, max_y)
        moves = 0
        new_grid = {}

        for location, space in grid.items():
            x, y = location
            new_x = next_location(x, max_x)
            new_location = (new_x, y)

            if space == '>':
                next = grid.get(new_location, '.')

                if next == '.':
                    moves += 1
                    new_grid[new_location] = space
                else:
                    new_grid[location] = space
            elif space == 'v':
                assert location not in new_grid

                # print(location, space)
                new_grid[location] = space
            else:
                pass

        # print('=============================')
        # print_grid(new_grid, max_x, max_y)
        assert sum(1 for item in grid.values() if item == '>') == sum(1 for item in new_grid.values() if item == '>'), "Lost '>'"
        assert sum(1 for item in grid.values() if item == 'v') == sum(1 for item in new_grid.values() if item == 'v'), "Lost 'v'"

        grid, new_grid = new_grid, {}

        for location, space in grid.items():
            x, y = location
            new_y = next_location(y, max_y)
            new_location = (x, new_y)

            if space == 'v':
                next = grid.get(new_location, '.')
                # next = grid[new_location]

                if next == '.':
                    moves += 1
                    assert location not in new_grid
                    new_grid[new_location] = space
                else:
                    assert location not in new_grid
                    new_grid[location] = space
            elif space == '>':
                assert location not in new_grid
                new_grid[location] = space

        # print('=============================')
        # print_grid(new_grid, max_x, max_y)
        assert sum(1 for item in grid.values() if item == '>') == sum(1 for item in new_grid.values() if item == '>'), "Lost '>'"
        assert sum(1 for item in grid.values() if item == 'v') == sum(1 for item in new_grid.values() if item == 'v'), "Lost 'v'"

        grid = new_grid

        if moves == 0:
            print('no moves!')
            break

    return step


def part2(data: list[str]) -> int:
    pass


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
