import fileinput
import json
import math
from functools import cmp_to_key
from itertools import zip_longest
from enum import IntEnum


class Comp(IntEnum):
    LT = -1
    EQ = 0
    GT = 1


def compare(left, right):
    types = type(left), type(right)

    if types == (int, int):
        if left < right:
            return Comp.LT
        elif left > right:
            return Comp.GT
        return Comp.EQ
    elif types == (list, int):
        return compare(left, [right])
    elif types == (int, list):
        return compare([left], right)
    elif types == (list, list):
        for sub_left, sub_right in zip_longest(left, right):
            if sub_left is None:
                return Comp.LT
            elif sub_right is None:
                return Comp.GT
            elif (result := compare(sub_left, sub_right)) == Comp.EQ:
                continue
            return result
        else:
            return Comp.EQ
    else:
        raise ValueError("Types: %s", types)


def part1(data):
    pairs = (tuple(json.loads(pairing.strip()) for pairing in pair.split('\n')) for pair in ''.join(data).strip().split('\n\n'))

    accumulator = 0

    for index, pair in enumerate(pairs, start=1):
        if (compare(*pair) != Comp.GT):
            accumulator += index

    return accumulator


def part2(data):
    divider_packets = [[[2]], [[6]]]

    packets = sorted([json.loads(packet) for packet in data if packet.strip()] + divider_packets, key=cmp_to_key(compare))

    return math.prod(map(lambda packet: packets.index(packet) + 1, divider_packets))


def main():
    print(result := part1(fileinput.input()))
    assert(result == 6568)
    print(result := part2(fileinput.input()))
    assert(result == 19493)


if __name__ == '__main__':
    main()
