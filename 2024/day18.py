import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
from heapq import heapify, heappop, heappush
from utils import *


def search(start, goal, corrupted):
    found = {}
    # queue = collections.deque([(0, start)])
    queue = [(goal.manhattan(start), 0, start)]
    max_x = goal.x
    max_y = goal.y

    while queue:
        # state = queue.popleft()
        state = heappop(queue)

        _, distance, location = state

        if found.get(location, math.inf) < distance:
            continue

        found[location] = distance

        if location == goal:
            break

        for neighbor in location.get_neighbors(offsets=Offset.cardinal()):
            if 0 <= neighbor.x <= max_x and 0 <= neighbor.y <= max_y and neighbor not in corrupted:
                # queue.append((distance + 1, neighbor))
                heappush(queue, (goal.manhattan(neighbor), (distance + 1), neighbor))

    return found.get(goal)


def part1(data):
    memory = [Point(*extract_ints(line)) for line in data]

    corrupted = set()
    start = Point(0, 0)
    goal, limit, max_x, max_y = Point(70, 70), 1024, 70, 70
    # goal, limit, max_x, max_y = Point(6, 6), 12, 6, 6

    for space in memory[:limit]:
        corrupted.add(space)

    return search(start, goal, corrupted)





    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
