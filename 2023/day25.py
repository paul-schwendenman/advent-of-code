import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
import igraph


def part1(data):
    # graph = collections.defaultdict(list)
    vertices = set()
    edges = set()

    for line in data:
        source, rest = line.rstrip().split(': ')
        vertices.add(source)
        for destination in rest.split(' '):
            # graph[source].append(destination)
            # graph[destination].append(source)
            vertices.add(destination)
            edges.add((source, destination))

            # print(f'{source} --> {destination}')

    graph = igraph.Graph()

    for vertex in vertices:
        graph.add_vertex(vertex)

    for edge in edges:
        graph.add_edge(*edge)

    cut = graph.mincut()

    left, right = cut.partition

    return len(left) * len(right)



    # pprint.pprint(graph)

    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    # print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
