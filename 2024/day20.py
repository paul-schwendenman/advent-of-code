import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from utils import *
from tqdm import tqdm


def print_grid(grid, max_x, max_y, path):
    for j in range(0, max_y+1):
        for i in range(0, max_x+1):
            # matches = [i for i in path if i[0] == (i, j)]
            matches = dict(path)
            if grid[(i, j)] in "SE":
                print(grid[(i, j)], end='')

            elif (i, j) in path:
                print('*', end='')

            elif (i,j) in matches:
                if matches[(i,j)] == Offset.RIGHT:
                    print('>', end='')
                elif matches[(i,j)] == Offset.LEFT:
                    print('<', end='')
                elif matches[(i,j)] == Offset.UP:
                    print('^', end='')
                elif matches[(i,j)] == Offset.DOWN:
                    print('v', end='')
                else:
                    print('*', end='')
            else:
                print(grid[(i, j)], end='')
        # print("".join(grid.get((i, j), '.') for i in range(0, max_x+1)))
        print('')
    print('')


def grid_search(start, grid, check_goal, get_next, is_next_valid, track_paths=True, strategy='bfs'):
    queue = collections.deque([(start,)])

    if strategy == 'bfs':
        pop_item = queue.popleft
    else:
        pop_item = queue.pop

    found = set()

    while queue:
        # print(f'queue: {len(queue)} {queue}')

        path = pop_item()
        # print(path)
        # print_grid(grid, 14, 14, path)
        # input()
        location = path[-1]
        current = path if track_paths else location

        if location not in grid:
            continue

        if current in found:
            continue

        if check_goal(location):
            # print('found')
            # print_grid(grid, 14, 14, path)
            found.add(current)
            continue

        for neighbor in get_next(location):
            if is_next_valid(location, neighbor, path):
                queue.append(path + (neighbor,))

    return found.pop()
    # return len(found)


def part1(data):
    grid, j, k, markers = parse_grid(data)

    start = markers['S'][0]
    end = markers['E'][0]

    def check_goal(location):
        return grid[location] == 'E'

    def get_next(location):
        yield from (location + dir for dir in Offset.cardinal())

    def is_valid(prev_location, next_location, path):
        if grid.get(next_location, '') != '#' and next_location not in path:
            return True
        return False

    path = grid_search(start, grid, check_goal, get_next, is_valid, track_paths=True, strategy='dfs')

    print(len(path))

    count = 0
    c = collections.Counter()
    # print_grid(grid, j, k, ())

    for a, b in tqdm(itertools.combinations(path, 2)):
        taxi = a.manhattan(b)

        if taxi != 2:
            continue

        steps = abs(path.index(a) - path.index(b))
        c[steps - taxi] += 1

        if taxi == 2 and steps - taxi >= 100:
            count += 1



    print(c)

    print(f'start: {start}\t end: {end}, {count}')
    return (count)
    pass


def part2(data):
    grid, j, k, markers = parse_grid(data)

    start = markers['S'][0]
    end = markers['E'][0]

    def check_goal(location):
        return grid[location] == 'E'

    def get_next(location):
        yield from (location + dir for dir in Offset.cardinal())

    def is_valid(prev_location, next_location, path):
        if grid.get(next_location, '') != '#' and next_location not in path:
            return True
        return False

    path = grid_search(start, grid, check_goal, get_next, is_valid, track_paths=True, strategy='dfs')

    print(len(path))

    count = 0
    c = collections.Counter()
    # print_grid(grid, j, k, ())

    path_dict = dict((point, index) for index, point in enumerate(path))

    for a, b in tqdm(itertools.combinations(path, 2)):
        taxi = a.manhattan(b)

        if taxi > 20:
            continue

        steps = abs(path_dict[a] - path_dict[b])
        c[steps - taxi] += 1

        if steps - taxi >= 100:
            count += 1



    print(c)

    # print(f'start: {start}\t end: {end}, {count}')
    return (count)
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
