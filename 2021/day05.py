import fileinput
from collections import defaultdict

def line_to_array(line):
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



def part1(lines):
    grid = defaultdict(int)

    for line in lines:
        for point in line_to_array(line):
            grid[point] += 1

    # print(grid)

    return sum(1 for key,value in grid.items() if value > 1)


def main():
    with fileinput.input() as input:
        lines = list(input)

    print(part1(lines))

if __name__ == '__main__':
    print(list(line_to_array('1,1 -> 1,3')))
    print(list(line_to_array('9,7 -> 7,7')))
    main()
