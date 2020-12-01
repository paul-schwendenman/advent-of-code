from enum import IntEnum
from collections import defaultdict, namedtuple
from typing import Tuple
from intcode import IntCode, open_program


Point = namedtuple('Point', 'x y')


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def rotate(self, clockwise: int):
        offset = 1 if clockwise else -1
        return Direction((self + offset) % 4)


def move_robot(location: Point, facing: Direction, clockwise: int) -> Tuple[Point, Direction]:
    facing = facing.rotate(clockwise)

    if facing == Direction.UP:
        location = Point(location.x, location.y - 1)
    elif facing == Direction.RIGHT:
        location = Point(location.x + 1, location.y)
    elif facing == Direction.DOWN:
        location = Point(location.x, location.y + 1)
    elif facing == Direction.LEFT:
        location = Point(location.x - 1, location.y)

    return location, facing


def main(initial_color=0, filename='input'):
    program = open_program(filename)
    computer = IntCode(program)

    halted = False
    grid = defaultdict(lambda: 0)
    location = Point(0, 0)
    grid[location] = initial_color
    facing = Direction.UP
    while not halted:
        computer.add_input(grid[location])
        halted = computer.run()

        color = computer.get_output()
        direction = computer.get_output()

        grid[location] = color
        location, facing = move_robot(location, facing, direction)

    print_grid(grid)

    return len(grid.keys())


def print_grid(grid):
    grid = grid.copy()
    min_x = min(point.x for point in grid.keys())
    max_x = max(point.x for point in grid.keys())
    min_y = min(point.y for point in grid.keys())
    max_y = max(point.y for point in grid.keys())

    for pos_y in range(min_y, max_y + 1):
        for pos_x in range(min_x, max_x + 1):
            print('#' if grid[Point(pos_x, pos_y)] else ' ', end='')
        print('')


if __name__ == "__main__":
    print(main(0))
    print(main(1))
