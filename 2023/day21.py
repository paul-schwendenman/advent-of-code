import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


class Point(typing.NamedTuple):
    x: int
    y: int

    def get_neighbors(self):
        # for offset in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)):
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            yield self + offset

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def proxy_location(self, max_x, max_y):
        return Point(self.x % max_x, self.y % max_y)


class State(typing.NamedTuple):
    location: Point
    steps: int = 0


class Spot(enum.Enum):
    GARDEN = '.'
    ROCK = '#'


def print_grid(grid, seen=set()):
    max_x = max(item.x for item in grid) + 1
    max_y = max(item.y for item in grid) + 1

    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in seen:
                print('O', end='')
            else:
                print('#' if grid[(x,y)] == Spot.ROCK else '.', end='')
        print('')
    print('')


def part1(data, max_steps=64):
    grid = {}
    start = None

    for y, line in enumerate(data):
        for x, chr in enumerate(line.rstrip()):
            if chr == 'S':
                start = Point(x, y)
                chr = '.'
            grid[Point(x, y)] = Spot(chr)

    queue = collections.deque([State(start)])
    seen = set()
    here = set()

    # print_grid(grid, seen)

    top_step = 0

    while queue:
        location, steps = queue.popleft()

        if location not in grid:
            continue

        if grid[location] == Spot.ROCK:
            continue

        if location in seen:
            continue

        if steps == max_steps:
            here.add(location)

        if steps > max_steps:
            continue

        # if steps > top_step:
        #     top_step = steps
        #     print(f'{steps} {len(queue)}')

        seen.add(location)

        for neighbor in location.get_neighbors():
            queue.append(State(neighbor, steps + 1))

    # print_grid(grid, here)

    return sum(1 for point in seen if start.manhattan(point) % 2 == 0)

def solve_part2(data, max_steps=64):
    grid = {}
    start = None

    for y, line in enumerate(data):
        for x, chr in enumerate(line.rstrip()):
            if chr == 'S':
                start = Point(x, y)
                chr = '.'
            grid[Point(x, y)] = Spot(chr)

    max_x = max(item.x for item in grid) + 1
    max_y = max(item.y for item in grid) + 1

    queue = collections.deque([State(start)])
    seen = set()
    here = set()

    # print_grid(grid, seen)

    top_step = 0

    while queue:
        location, steps = queue.popleft()

        if (proxy := location.proxy_location(max_x, max_y)) not in grid:
            continue

        if grid[proxy] == Spot.ROCK:
            continue

        if location in seen:
            continue

        if steps == max_steps:
            here.add(location)

        if steps > max_steps:
            continue

        # if steps > top_step:
        #     top_step = steps
        #     print(f'{steps} {len(queue)}')

        seen.add(location)

        for neighbor in location.get_neighbors():
            queue.append(State(neighbor, steps + 1))

    # print_grid(grid, here)

    return sum(1 for point in seen if start.manhattan(point) % 2 == 0)


def part2(data, max_steps=26501365):


    grid = {}
    start = None

    for y, line in enumerate(data):
        for x, chr in enumerate(line.rstrip()):
            if chr == 'S':
                start = Point(x, y)
                chr = '.'
            grid[Point(x, y)] = Spot(chr)

    max_x = max(item.x for item in grid) + 1
    max_y = max(item.y for item in grid) + 1

    print(f'{max_x=} {max_y=} {max_steps=} {max_steps/max_x}')

    # queue = collections.deque([])
    queue = collections.deque([State(start)])
    seen = set()
    here = set()

    # print_grid(grid, seen)

    # top_step = 0
    garden_count = sum(1 for spot in grid.values() if spot == Spot.GARDEN)
    rock_count = sum(1 for spot in grid.values() if spot == Spot.ROCK)

    print(f'{garden_count=} {rock_count=}')

    assert (max_x * max_y) == garden_count + rock_count

    n = 0
    values = []

    for step in itertools.count():
        next_queue = collections.deque()
        while queue:
            location, steps = queue.popleft()

            if (proxy := location.proxy_location(max_x, max_y)) not in grid:
                raise ValueError("Invalid", location, proxy)

            if grid[proxy] == Spot.ROCK:
                continue

            if location in seen:
                continue

            if steps == max_steps:
                here.add(location)

            if steps > max_steps:
                continue

            if len(seen) == (garden_count * 9):
                print(f'{steps=}')
                break

            # if (steps - 65) % 131 == 0:
            #     print(f'{steps:4d}: {len([1 for point in seen if start.manhattan(point) % 2 == 0])}')

            # if steps > top_step:
            #     top_step = steps
            #     print(f'{steps} {len(queue)}')

            if steps % max_x == max_steps % max_x:
                pass


        seen.add(location)

        for neighbor in location.get_neighbors():
            next_queue.append(State(neighbor, steps + 1))

        if step % (max_x) == max_steps % (max_x):
            print(f'{len([1 for point in seen if start.manhattan(point) % 2 == 0])}')
            values.append(len([1 for point in seen if start.manhattan(point) % 2 == 0]))
            n += 1

        if n == 3:
            break
        queue = next_queue

    # print_grid(grid, here)

    # print(f'{len([1 for point in seen if start.manhattan(point) % 2 == 1])}')

    print(f'{[b - a for a, b in itertools.pairwise(values)]}')

    print(f'({max_steps} - {max_x//2}) / {max_x} == {(max_steps - 65) / 131}')

    return len(here)

def part3(data):
    grid = {}
    start = None

    for y, line in enumerate(data):
        for x, chr in enumerate(line.rstrip()):
            if chr == 'S':
                start = Point(x, y)
                chr = '.'
            grid[Point(x, y)] = Spot(chr)

    max_x = max(item.x for item in grid) + 1
    max_y = max(item.y for item in grid) + 1

    active = set([start])
    for step in range(50):
        for point in active:
            pass
        active = set(itertools.chain(p for p in active if grid[p.proxy_location(max_x, max_y)]))

    print(f'{len([1 for point in active if start.manhattan(point) % 2 == 0])}')


def solve(n):
    n0 = 3795
    n1 = 34785
    n2 = 95981
    n3 = 188951

    v0 = n1 - n0
    v1 = n2 - n1
    v2 = n3 - n2

    print([v0, v1, v2])

    a0 = v1 - v0
    a1 = v2 - v1

    print([a0, a1])

    '''
    https://www.wolframalpha.com/input?i=quadratic+fit+calculator&assumption=%7B%22F%22%2C+%22QuadraticFitCalculator%22%2C+%22data3x%22%7D+-%3E%22%7B0%2C+1%2C+2%7D%22&assumption=%7B%22F%22%2C+%22QuadraticFitCalculator%22%2C+%22data3y%22%7D+-%3E%22%7B3795%2C+34785%2C+95981%7D%22
    3795 + 15887 x + 15103 x^2
    '''
    v0, a0 = 15887, 15103
    print(f'f(x) = {a0} * x^2 + {v0} * x + {n0}')
    return n0 + v1*n + n * a0

    assert a1 == a0


def main():
    print(part1(fileinput.input(), 64))

    goal = 26501365
    data = list(fileinput.input())
    n = 0
    for steps in itertools.count(1):
        if steps % 262 == goal % 262:
        # if steps % 131 == goal % 131:
            print(f'{steps:4d} {steps % 131} {solve_part2(data, steps)}')
            n += 1
        if n > 3:
            break

    print(solve(goal // 131))
    # print(part2(fileinput.input()))
    # print(part3(fileinput.input()))


if __name__ == '__main__':
    main()
