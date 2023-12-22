import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
import dataclasses


class Point(typing.NamedTuple):
    x: int
    y: int
    z: int

    def drop(self):
        return Point(self.x, self.y, self.z - 1)

@dataclasses.dataclass
class Shape:
    corner_1: Point
    corner_2: Point

    def top(self):
        min_x = min(self.corner_1.x, self.corner_2.x)
        min_y = min(self.corner_1.y, self.corner_2.y)
        max_x = max(self.corner_1.x, self.corner_2.x) + 1
        max_y = max(self.corner_1.y, self.corner_2.y) + 1

        max_z = max(self.corner_1.z, self.corner_2.z)

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                yield Point(x, y, max_z)

    def bottom(self):
        min_x = min(self.corner_1.x, self.corner_2.x)
        min_y = min(self.corner_1.y, self.corner_2.y)
        max_x = max(self.corner_1.x, self.corner_2.x) + 1
        max_y = max(self.corner_1.y, self.corner_2.y) + 1

        min_z = min(self.corner_1.z, self.corner_2.z)

        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                yield Point(x, y, min_z)

    def on_bottom(self):
        return 1 == min(self.corner_1.z, self.corner_2.z)

    def drop(self):
        self.corner_1 = self.corner_1.drop()
        self.corner_2 = self.corner_2.drop()

    def __hash__(self):
        return hash(self.corner_1 + self.corner_2)


class Brick(typing.NamedTuple):
    x1: int
    y1: int
    z1: int
    x2: int
    y2: int
    z2: int

    def range_x(self):
        return range(self.x1, self.x2 + 1)

    def range_y(self):
        return range(self.y1, self.y2 + 1)

    def fall(self, dz):
        return Brick(self.x1, self.y1, self.z1 - dz, self.x2, self.y2, self.z2 - dz)


def part1_old(data):
    shapes = []

    for line in data:
        one, two = line.split('~')
        one = [int(num) for num in one.split(',')]
        two = [int(num) for num in two.split(',')]
        corner_1 = Point(*one)
        corner_2 = Point(*two)
        shape = Shape(corner_1, corner_2)
        shapes.append(shape)

    for shape in shapes:
        assert shape.corner_1.x <= shape.corner_2.x
        assert shape.corner_1.y <= shape.corner_2.y
        assert shape.corner_1.z <= shape.corner_2.z

    shapes = list(sorted(shapes, key=lambda item: item.corner_1.z))

    changed = True
    supported_by = collections.defaultdict(list)
    supporting = collections.defaultdict(list)


    while changed:
        changed = False
        hit = set()

        for shape in shapes:
            if shape.on_bottom():
                continue
            touching = False
            for shape2 in shapes:
                if len(set(shape.bottom()) & set(shape2.top())):
                    touching = True
                    hit.add((shape2.corner_1, shape2.corner_2))
                    supported_by[shape].append(shape2)
                    supporting[shape2].append(shape)

            if not touching:
                # print('dropping')
                shape.drop()
                changed = True

    print(f'{len(shapes)} - {len(hit)} = {len(shapes) - len(hit)}')

    acc = 0
    for shape in shapes:
        if len(supporting[shape]) == 0:
            acc += 1
        for shape2 in supporting[shape]:
            if len(supported_by[shape2]) > 1:
                acc + 1
                break

    print(f'{acc=}')




    pass


def extract_ints(str):
    for num in re.findall(r'\d+', str):
        yield int(num)


def gravity_brick(peaks: dict[tuple[int, int], int], brick: Brick):
    ceiling = max(peaks[(x, y)] for x in brick.range_x() for y in brick.range_y())
    peak = max(peaks[(x, y)] for x in range(brick[0], brick[3] + 1) for y in range(brick[1], brick[4] + 1))
    assert peak == ceiling

    dz = max(brick.z1 - ceiling - 1, 0)
    dz = max(brick[2] - peak - 1, 0)

    return brick.fall(dz), dz


def gravity(bricks):
    peaks = collections.defaultdict(int)
    new_bricks = []
    changed = 0

    for brick in bricks:
        new_brick, dz = gravity_brick(peaks, brick)

        if dz > 0:
            changed += 1
        new_bricks.append(new_brick)

        for y in new_brick.range_y():
            for x in new_brick.range_x():
                peaks[(x, y)] = new_brick.z2

    return changed, new_bricks

def part1(data):
    bricks = sorted((Brick(*extract_ints(line)) for line in data), key=lambda item: item.z1)

    _, settled_bricks = gravity(bricks)
    acc = 0

    for index in range(len(settled_bricks)):
        before, _, after = settled_bricks[:index], settled_bricks[index:index+1], settled_bricks[index + 1:]

        missing = before + after

        distance, _ = gravity(missing)

        if distance == 0:
            acc += 1

    return acc
    print(bricks)

def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
