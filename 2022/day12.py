import fileinput
from collections import namedtuple, defaultdict, deque

class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

    @property
    def neighbors(self):
        for pair in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            yield self + pair


Step = namedtuple('Step', 'point step')


def solve_maze(start, goal, grid, tracker={}, path=[]):
    def check_neighbor(start, end):
        if end in path:
            return False
        elif end not in grid:
            return False
        elif abs(grid[start] - grid[end]) > 1:
            return False
        return True

    if start == goal:
        return path

    return min(
        (answer := solve_maze(neighbor, goal, grid, path + [start])
        for neighbor in start.neighbors
        if check_neighbor(start, neighbor)),
        key=lambda value: len(value) if value is not None else 1_000_000
    )


def bfs(grid, start, end):
    def check_neighbor(start, end):
        # if end in grid and abs(ord(grid[start]) - ord(grid[end])) <= 1:
        if end in grid and (ord(grid[end]) - ord(grid[start])) <= 1:
            return True
        return False

    seen = set()

    todo = deque([Step(start, 0)])

    while todo:
        position, step = todo.popleft()

        if position == end:
            return step
        if position in seen:
            continue
        seen.add(position)

        for neighbor in position.neighbors:
            if check_neighbor(position, neighbor):
                todo.append(Step(neighbor, step + 1))


def part1(data):
    grid = {}
    start = None
    end = None

    for j, line in enumerate(data):
        for i, char in enumerate(line.rstrip()):
            here = Point(i, j)

            if char == 'S':
                start = here
                grid[here] = 'a'
            elif char == 'E':
                end = here
                grid[here] = 'z'
            else:
                grid[here] = char


    return bfs(grid, start, end)


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
