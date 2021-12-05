import fileinput
from collections import defaultdict
from itertools import repeat


def print_grid(grid):
    for j in range(10):
        print(''.join('.' if grid[(i,j)] == 0 else str(grid[(i, j)]) for i in range(10)))


def line_to_array(line, include_diagonals = False):
    [start, end] = line.split(' -> ')
    start_x, start_y = map(int, start.split(','))
    end_x, end_y = map(int, end.split(','))

    if not include_diagonals and (start_x != end_x and start_y != end_y):
        return []

    x_step = 1 if end_x >= start_x else -1
    y_step = 1 if end_y >= start_y else -1

    if start_x == end_x:
        x_values = repeat(start_x)
    else:
        x_values = range(start_x, end_x + x_step, x_step)

    if start_y == end_y:
        y_values = repeat(start_y)
    else:
        y_values = range(start_y, end_y + y_step, y_step)

    yield from zip(x_values, y_values)



def part1(lines):
    grid = defaultdict(int)

    for line in lines:
        for point in line_to_array(line):
            grid[point] += 1

    return sum(1 for value in grid.values() if value > 1)


def part2(lines):
    grid = defaultdict(int)

    for line in lines:
        for point in line_to_array(line, include_diagonals=True):
            grid[point] += 1

    return sum(1 for value in grid.values() if value > 1)


def main():
    with fileinput.input() as input:
        lines = list(input)

    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    # print(list(line_to_array('1,1 -> 1,3')))
    # print(list(line_to_array('9,7 -> 7,7')))
    # print(list(line_to_array('1,1 -> 3,3', include_diagonals=True)))
    # print(list(line_to_array('9,7 -> 7,9', include_diagonals=True)))
    main()
