import fileinput
from collections import defaultdict, namedtuple
from enum import Enum

class Display(Enum):
    AIR = '.'
    ROCK = "#"
    STABLE_SAND = 'O'
    SOURCE = '+'

    def __str__(self):
        return self.value


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def points_below(self):
        yield Point(self.x, self.y + 1)
        yield Point(self.x - 1, self.y + 1)
        yield Point(self.x + 1, self.y + 1)


def parse_line(line):
    return [Point(*[int(coord) for coord in point.split(',')]) for point in line.split('->')]


def generate_line(start, end):
    if start.x == end.x:
        for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
            yield Point(start.x, y)
    elif start.y == end.y:
        for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
            yield Point(x, start.y)
    else:
        ValueError('Diagonal line')


def plot_points(points, grid):
    for start, end in zip(points[:], points[1:]):
        for point in generate_line(start, end):
            grid[point] = Display.ROCK

    return grid



def parse_input(data):
    grid = {
        Point(500, 0): Display.SOURCE
    } #defaultdict()
    for line in data:
        points = parse_line(line)

        grid = plot_points(points, grid)

    return grid


def print_grid(grid):
    rocks = grid.keys()
    min_x = min(p.x for p in rocks) - 1
    max_x = max(p.x for p in rocks) + 2
    min_y = min(p.y for p in rocks) - 1
    max_y = max(p.y for p in rocks) + 2

    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            print(str(grid.get(Point(x, y), Display.AIR)), end='')
        print('')



def part1(data):
    grid = parse_input(data)

    rocks = grid.keys()
    max_y_rock = max(p.y for p in rocks)


    kill_switch = False

    while not kill_switch:
        sand = Point(500, 0)
        while not kill_switch:
            for next_spot in sand.points_below():
                if next_spot.y > max_y_rock:
                    kill_switch = True
                    break
                elif next_spot not in grid:
                    sand = next_spot
                    break
            else:
                grid[sand] = Display.STABLE_SAND
                break

        # print_grid(grid)
        # input()

    return sum(1 for point in grid.values() if point == Display.STABLE_SAND)



    print_grid(grid)
    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
