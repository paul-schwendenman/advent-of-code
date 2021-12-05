import fileinput
from collections import defaultdict

def line_to_array(line, include_diagonals = False):
    [start, end] = line.split(' -> ')
    start_x, start_y = map(int, start.split(','))
    end_x, end_y = map(int, end.split(','))

    if start_x == end_x:
        if start_y > end_y:
            start_y, end_y = end_y, start_y
        for i in range(start_y, end_y + 1):
            yield (start_x, i)
    elif start_y == end_y:
        if start_x > end_x:
            start_x, end_x = end_x, start_x
        for i in range(start_x, end_x + 1):
            yield (i, start_y)
    elif include_diagonals:
        x_step = 1 if end_x > start_x else -1
        y_step = 1 if end_y > start_y else -1

        x_values = range(start_x, end_x + x_step, x_step)
        y_values = range(start_y, end_y + y_step, y_step)

        for pair in zip(x_values, y_values):
            yield pair




def part1(lines):
    grid = defaultdict(int)

    for line in lines:
        for point in line_to_array(line):
            grid[point] += 1

    #print(grid)
    # print_grid(grid)

    return sum(1 for key,value in grid.items() if value > 1)

def part2(lines):
    grid = defaultdict(int)

    for line in lines:
        for point in line_to_array(line, include_diagonals=True):
            grid[point] += 1

    #print(grid)
    # print_grid(grid)

    return sum(1 for key,value in grid.items() if value > 1)


def print_grid(grid):
    for j in range(10):
        print(''.join('.' if grid[(i,j)] == 0 else str(grid[(i, j)]) for i in range(10)))

def main():
    with fileinput.input() as input:
        lines = list(input)

    print(part1(lines))
    print(part2(lines))

if __name__ == '__main__':
    print(list(line_to_array('1,1 -> 1,3')))
    print(list(line_to_array('9,7 -> 7,7')))
    print(list(line_to_array('1,1 -> 3,3')))
    print(list(line_to_array('9,7 -> 7,9')))
    main()
