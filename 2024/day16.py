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

    states = [(0, ((start, facing), ))]
    heapify(states)

    found = {}

    print_grid(grid, j, k, path=(start,))

    while states:
        print(f'------- new state {len(states)} ---------')
        # input()
        state = heappop(states)

        # if len(states) > 10_000:
        #     print(f'state: {state}')

        cost, path = state
        print(f'path: {path}')
        location, facing = path[-1]

        print(f'cost: {cost} facing: {facing} path: {path[-3:]}')
        print_grid(grid, j, k, path)

        if found.get((location, facing.value), math.inf) <= cost:
            print(f'skipping, easier path found: {location}')
            continue
        else:
            print(f'new location: {found.get(location)} = {cost}')
            found[(location, facing.value)] = cost

        if location == end:
            print(f'found: {location} {len(path)} {path}')
            print_grid(grid, j, k, path)
            break

        if grid.get(next_location := location + facing, '#') != '#':
            print(f'forward: {location} -> {next_location} ({cost+1})')
            heappush(states, ((cost + 1, path + ((next_location, facing), ))))
        else:
            pass
            print(f'wall: {location} + {facing} = {next_location} -> {grid.get(next_location)}')

        for next_facing in (facing.rotate(), facing.rotate(True)):
            print(f'turning {facing} -> {next_facing} {location} {cost + 1000}')
            heappush(states, ((cost + 1000), path + ((location, next_facing), )))


    return cost



    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
