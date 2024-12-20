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


def grid_search(start, grid, check_goal, get_next, is_next_valid, track_paths=True, strategy='bfs'):
    queue = collections.deque([(start,)])

    if strategy == 'bfs':
        pop_item = queue.popleft
    else:
        pop_item = queue.pop

    found = set()

    while queue:
        path = pop_item()
        location = path[-1]
        current = path if track_paths else location

        if location not in grid:
            continue

        if current in found:
            continue

        if check_goal(location):
            found.add(current)
            continue

        for neighbor in get_next(location):
            if is_next_valid(location, neighbor, path):
                queue.append(path + (neighbor,))

    return found.pop()


def part1(data):
    grid, _, _, markers = parse_grid(data)

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
    path_dict = dict((point, index) for index, point in enumerate(path))

    count = 0
    c = collections.Counter()

    for a, b in tqdm(itertools.combinations(path, 2)):
        taxi = a.manhattan(b)

        if taxi != 2:
            continue

        steps = abs(path_dict[a] - path_dict[b])
        c[steps - taxi] += 1

        if taxi == 2 and steps - taxi >= 100:
            count += 1

    return count


def part2(data):
    grid, _, _, markers = parse_grid(data)

    start = markers['S'][0]

    def check_goal(location):
        return grid[location] == 'E'

    def get_next(location):
        yield from (location + dir for dir in Offset.cardinal())

    def is_valid(prev_location, next_location, path):
        if grid.get(next_location, '') != '#' and next_location not in path:
            return True
        return False

    path = grid_search(start, grid, check_goal, get_next, is_valid, track_paths=True, strategy='dfs')

    count = 0
    c = collections.Counter()

    path_dict = dict((point, index) for index, point in enumerate(path))

    for a, b in tqdm(itertools.combinations(path, 2)):
        taxi = a.manhattan(b)

        if taxi > 20:
            continue

        steps = abs(path_dict[a] - path_dict[b])
        c[steps - taxi] += 1

        if steps - taxi >= 100:
            count += 1

    return (count)


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
