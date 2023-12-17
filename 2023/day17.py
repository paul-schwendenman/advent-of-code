import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
import heapq

class Point(typing.NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])


class Direction(tuple, enum.Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class State(typing.NamedTuple):
    loss: int
    location: Point
    prev_moves: tuple[Direction, Direction, Direction]


def part1(data):
    grid = {}
    for j, line in enumerate(data):
        for i, loss in enumerate(line.rstrip()):
            grid[Point(i, j)] = int(loss)

    start = Point(0, 0)
    end = Point(i, j)
    min_loss = math.inf

    queue = [State(0, start, tuple())]
    spots = {}

    while len(queue) > 0:
        loss, location, prev_moves = heapq.heappop(queue)

        if (location, prev_moves) in spots:
            assert loss >= spots[(location, prev_moves)]
            continue

        spots[(location, prev_moves)] = loss

        if loss > min_loss:
            continue

        if location == end:
            # print('found the end')
            min_loss = min(min_loss, loss)
            continue

        for direction in (Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST):
            next_location = location + direction
            if next_location not in grid:
                continue

            if len(prev_moves) > 1 and (prev_moves[-1][0] + direction[0], prev_moves[-1][1] + direction[1]) == (0, 0):
                continue

            if len(prev_moves) == 3 and all(map(lambda item: item == direction, prev_moves)):
                continue

            next_loss = loss + grid[next_location]
            next_directions = (prev_moves + (direction,))[-3:]
            if len(next_directions) > 3:
                raise ValueError("Out of bounds")

            heapq.heappush(queue, State(next_loss, next_location, next_directions))

    return min_loss


def part2(data):
    grid = {}
    for j, line in enumerate(data):
        for i, loss in enumerate(line.rstrip()):
            grid[Point(i, j)] = int(loss)

    start = Point(0, 0)
    end = Point(i, j)
    min_loss = math.inf

    queue = [State(0, start, tuple())]
    spots = {}

    while len(queue) > 0:
        loss, location, prev_moves = heapq.heappop(queue)

        if (location, prev_moves) in spots:
            assert loss >= spots[(location, prev_moves)]
            continue

        spots[(location, prev_moves)] = loss

        if loss > min_loss:
            continue

        if location == end:
            min_loss = min(min_loss, loss)
            continue

        for direction in (Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST):
            next_location = location + direction
            if next_location not in grid:
                continue

            if len(prev_moves) > 1 and (prev_moves[-1][0] + direction[0], prev_moves[-1][1] + direction[1]) == (0, 0):
                continue

            if len(prev_moves) == 10 and all(map(lambda item: item == direction, prev_moves)):
                continue

            if len(prev_moves) >= 1 and not (prev_moves[-1] == direction or len(set(prev_moves[-4:])) == 1):
                continue

            next_loss = loss + grid[next_location]
            next_directions = (prev_moves + (direction,))[-10:]

            heapq.heappush(queue, State(next_loss, next_location, next_directions))

    return min_loss


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
