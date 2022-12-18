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
    # internal_air = 0
    cubes = {Cube(*extract_ints(line)) for line in data}
    air_pockets = set()

    for cube in cubes:
        count += sum(1 for c in cube.neighbors() if c not in cubes)
        air_pockets |= {c for c in cube.neighbors() if c not in cubes}

    for air_pocket in air_pockets:
        if all(apn in cubes for apn in air_pocket.neighbors()):
            count -= 6



    return count
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
