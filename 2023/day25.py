import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
import karger


def part1(data):
    graph = collections.defaultdict(list)
    # print('flowchart TD')
    edges = set()

    for line in data:
        source, rest = line.rstrip().split(': ')
        for destination in rest.split(' '):
            graph[source].append(destination)
            graph[destination].append(source)
            edges.add((source, destination))

            # print(f'{source} --> {destination}')

    k_graph = karger.Graph(len(graph.keys()), len(edges))
    nums = {name: i for i, name in enumerate(graph.keys())}

    for edge in edges:
        a = nums[edge[0]]
        b = nums[edge[1]]

        k_graph.edge.append(karger.Edge(a, b))

    res = karger.kargerMinCut(k_graph)

    print("Found: ", res)



    # pprint.pprint(graph)

    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
