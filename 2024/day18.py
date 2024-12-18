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


def part1(data):
    memory = [Point(*extract_ints(line)) for line in data]

    corrupted = set()
    start = Point(0, 0)
    # goal, limit, max_x, max_y = Point(70, 70), 1024, 70, 70
    goal, limit, max_x, max_y = Point(6, 6), 12, 6, 6

    for space in memory[:limit]:
        corrupted.add(space)

    found = {}
    queue = collections.deque([(0, start)])

    while queue:
        state = queue.popleft()

        distance, location = state

        if found.get(location, math.inf) < distance:
            continue

        if location in corrupted:
            continue

        found[location] = distance

        for neighbor in location.get_neighbors(offsets=Offset.cardinal()):
            if 0 <= neighbor.x <= max_x and 0 <= neighbor.y <= max_y:
                queue.append((distance + 1, neighbor))

    return found[goal]




    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
