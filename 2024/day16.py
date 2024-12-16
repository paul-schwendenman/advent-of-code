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
from heapq import heapify, heappop, heappush


def print_grid(grid, max_x, max_y, path):
    for j in range(0, max_y+1):
        for i in range(0, max_x+1):
            # matches = [i for i in path if i[0] == (i, j)]
            matches = dict(path)
            if grid[(i, j)] in "SE":
                print(grid[(i, j)], end='')

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


def part1(data):
    grid, j, k, markers = parse_grid(data)

    start = markers['S'][0]
    end = markers['E'][0]
    facing = Offset.EAST

    states = [(0, start, facing, [(start, facing)])]
    heapify(states)

    found = {}

    # print_grid(grid, j, k, path=(start,))

    while states:
        state = heappop(states)
        # print(f'{state}')

        cost, location, facing, path = state
        # print_grid(grid, j, k, path)
        # input()

        if location in found:
            continue
        found[location] = cost

        if grid[location] == '#':
            continue

        heappush(states, (cost + 1, location + facing, facing, path + [(location + facing, facing)]))

        for next_facing in (facing.rotate(False), facing.rotate(True)):

            heappush(states, (cost + 1001, location + next_facing, next_facing, path + [(location + next_facing, next_facing)]))

    # pprint.pprint(found)

    return found[end]



def solve(grid, start, end):
    facing = Offset.EAST
    states = [(0, start, facing, [(start, facing)])]
    heapify(states)

    found = collections.defaultdict(lambda: math.inf)
    points = collections.defaultdict(set)

    # print_grid(grid, j, k, path=(start,))

    while states:
        state = heappop(states)
        # print(f'{state}')

        cost, location, facing, path = state
        # print_grid(grid, j, k, path)
        # input()

        if found[location] < cost:
            continue
        found[location] = cost
        points[location] |= set(i[0] for i in path)

        if grid[location] == '#':
            continue

        heappush(states, (cost + 1, location + facing, facing, path + [(location + facing, facing)]))

        for next_facing in (facing.rotate(False), facing.rotate(True)):
            heappush(states, (cost + 1001, location + next_facing, next_facing, path + [(location + next_facing, next_facing)]))

    return found[end], points[end]


def part2(data):
    grid, j, k, markers = parse_grid(data)

    start = markers['S'][0]
    end = markers['E'][0]

    score, path = solve(grid, start, end)

    for spot in list(path):
        if spot in (start, end):
            continue
        grid[spot] = '#'

        cost, p = solve(grid, start, end)

        if cost == score:
                path |= p

        grid[spot] = '.'




    return score, len(path)
    pass


def main():
    # print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
