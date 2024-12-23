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
    pairs = [line.rstrip().split('-') for line in data]

    connections = collections.defaultdict(set)
    count = 0

    for a, b in pairs:
        connections[a].add(b)
        connections[b].add(a)

    threes = set()

    for a, b, c in itertools.combinations(connections.keys(), r=3):
        if (a in (connections[b] & connections[c])
            and b in (connections[a] & connections[c])
            and c in (connections[b] & connections[a])):
            if any(item[0] == 't' for item in (a,b,c)):
                count += 1

            # print(a, b, c)
            pass

    # for a, b in pairs:
    #     union = connections[a] & connections[b]
    #     intersection = connections[a] | connections[b]
    #     # print(f'{a} & {b}: {union} {intersection}')

    #     if len(union) == 1:
    #         print(f'{a} & {b}: {union} {intersection} {union | set((a, b))}')
    #         threes.add(tuple(sorted([a, b, union.pop()])))

    # count = sum(any(item[0] == 't' for item in three) for three in threes)

    # print(len(threes))

    # for three in threes:
    #     if any(item[0] == 't' for item in three):
    #         print(three)

    return count

    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
