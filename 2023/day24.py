import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
import decimal


class Point(typing.NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1], self.z + other[2])


class Hailstone(typing.NamedTuple):
    x: int
    y: int
    z: int
    dx: int
    dy: int
    dz: int


def cross(stone1: Hailstone, stone2: Hailstone):
    x1, x2 = stone1.x, stone1.x + stone1.dx
    x3, x4 = stone2.x, stone2.x + stone2.dx
    y1, y2 = stone1.y, stone1.y + stone1.dy
    y3, y4 = stone2.y, stone2.y + stone2.dy

    dx1 = x1 - x2
    dx2 = x3 - x4
    dy1 = y1 - y2
    dy2 = y3 - y4

    determinate = ((dx1 * dy2) - (dy1 * dx2))
    if determinate == 0:
        raise ValueError('lines do not cross')

    px = (((x1 * y2) - (y1 * x2)) * (dx2) - (dx1) * ((x3 * y4) - (y3*x4))) / determinate
    py = (((x1 * y2) - (y1 * x2)) * (dy2) - (dy1) * ((x3 * y4)- (y3*x4))) / determinate
    valid = (px>x1)==(x2>x1) and (px>x3)==(x4>x3)

    return (px, py), valid


def extract_ints(str):
    for num in re.findall(r'-?\d+', str):
        yield int(num)


def parse_input(data):
    hailstones: list[Hailstone] = []

    for line in data:
        x, y, z, dx, dy, dz = extract_ints(line)

        hailstones.append(Hailstone(x, y, z, dx, dy, dz))

    return hailstones


def part1(data, bounds):
    acc = 0
    hailstones = parse_input(data)


    for a, b in itertools.combinations(hailstones, 2):
        try:
            (x, y), valid = cross(a, b)

            if valid and bounds[0] <= x <= bounds[1] and bounds[0] <= y <= bounds[1]:
                acc += 1

        except ValueError:
            pass

    return acc


def part2(data):
    import z3

    hailstones = parse_input(data)
    solver = z3.Solver()

    x, y, z = z3.Int('x'), z3.Int('y'), z3.Int('z')
    dx, dy, dz = z3.Int('dx'), z3.Int('dy'), z3.Int('dz')
    times = [z3.Int(f'T{i}') for i in range(len(hailstones))]

    for hailstone, time in zip(hailstones, times):
        solver.add(x + time * dx - hailstone.x - hailstone.dx * time == 0)
        solver.add(y + time * dy - hailstone.y - hailstone.dy * time == 0)
        solver.add(z + time * dz - hailstone.z - hailstone.dz * time == 0)

    result = solver.check()
    model = solver.model()

    return model.eval(x + y + z)


def main():
    bounds = (200000000000000, 400000000000000)
    print(part1(fileinput.input(), bounds))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
