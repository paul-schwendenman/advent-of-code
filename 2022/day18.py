import fileinput
from helper import *

class Cube(namedtuple('Cube', 'x y z')):
    __slots__ = ()

    def __add__(self, other):
        return Cube(self.x + other[0], self.y + other[1], self.z + other[2])

    def neighbors(self):
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                for z in (-1, 0, 1):
                    if abs(x) + abs(y) + abs(z) in (1,):
                        yield self + (x, y, z)


def part1(data):
    count = 0
    cubes = {Cube(*extract_ints(line)) for line in data}

    for cube in cubes:
        count += sum(1 for c in cube.neighbors() if c not in cubes)
        pass

    return count


def part2(data):
    count = 0

    all_spaces = {Cube(x, y, z) for x in range(20) for y in range(20) for z in range(20)}
    cubes = {Cube(*extract_ints(line)) for line in data}

    assert len(cubes) == len(all_spaces & cubes)

    air_pockets = set()

    for cube in cubes:
        count += sum(1 for c in cube.neighbors() if c not in cubes)
        air_pockets |= {c for c in cube.neighbors() if c not in cubes}


    empty = all_spaces - cubes
    queue = deque([Cube(0, 0, 0)])

    while queue:
        pass
        air = queue.popleft()
        if air in empty:
            empty.remove(air)
            queue.extend(air.neighbors())

    for cube in empty:
        count -= sum(1 for c in cube.neighbors() if c in cubes)

    return count


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
