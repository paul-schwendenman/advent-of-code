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


def extract_ints(str):
    for num in re.findall(r'\d+', str):
        yield int(num)


def gravity_brick(peaks, brick):
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


def part2(data):
    bricks = sorted((Brick(*extract_ints(line)) for line in data), key=lambda item: item.z1)

    _, settled_bricks = gravity(bricks)
    acc = 0

    for index in range(len(settled_bricks)):
        before, _, after = settled_bricks[:index], settled_bricks[index:index+1], settled_bricks[index + 1:]

        missing = before + after

        distance, _ = gravity(missing)

        if distance > 0:
            acc += distance

    return acc


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
