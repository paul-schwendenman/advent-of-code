import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing

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
    location: Point
    loss: int
    prev_moves: tuple[Direction, Direction, Direction]


def part1(data):
    grid = {}
    for j, line in enumerate(data):
        for i, loss in enumerate(line.rstrip()):
            grid[Point(i, j)] = int(loss)

    start = Point(0, 0)
    end = Point(i, j)
    min_loss = math.inf

    queue = collections.deque([State(start, 0, tuple())])

    while len(queue) > 0:
        print(f'states: {len(queue)}')
        location, loss, prev_moves = queue.popleft()

        if loss > min_loss:
            print(f'path exceeds loss: {loss} > {min_loss}')
            continue

        if location == end:
            print('found the end')
            min_loss = min(min_loss, loss)
            continue

        for direction in (Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST):
            next_location = location + direction
            if next_location not in grid:
                # print(f'moving {direction} is out of bounds: {next_location}')
                continue

            if len(prev_moves) > 1 and (prev_moves[-1] + direction) == (0, 0):
                continue

            if len(prev_moves) == 3 and all(map(lambda item: item == direction, prev_moves)):
                continue

            next_loss = loss + grid[location]
            next_directions = prev_moves[-3:] + (direction,)

            queue.append(State(next_location, next_loss, next_directions))



        pass
    pass
    return min_loss

def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
