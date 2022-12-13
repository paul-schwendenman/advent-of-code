import fileinput
import json
from functools import cmp_to_key
from enum import IntEnum

class Comp(IntEnum):
    LT = -1
    EQ = 0
    GT = 1


def compare(a, b):
    types = type(a), type(b)
    # print(a, b, types)

    if types == (int, int):
        if a < b:
            return Comp.LT
        elif a > b:
            return Comp.GT
        return Comp.EQ
    elif types == (list, int):
        return compare(a, [b])
    elif types == (int, list):
        return compare([a], b)
    elif types == (list, list):
        for i in range(max(size_a := len(a), size_b := len(b))):
            if size_a <= i:
                return Comp.LT
            elif size_b <= i:
                return Comp.GT
            else:
                if (result := compare(a[i], b[i])) == Comp.EQ:
                    continue
                return result
        else:
            return Comp.EQ
    else:
        raise ValueError("Types: %s", types)


def part1(data):
    pairs = (tuple(eval(pairing.strip()) for pairing in pair.split('\n')) for pair in ''.join(data).strip().split('\n\n'))
    count = 0
    correct_pairs = []

    for i, pair in enumerate(pairs):
        if (compare(*pair) != Comp.GT):
            count += 1
            correct_pairs.append(i)

    return sum(correct_pairs) + len(correct_pairs)


def part2(data):
    packets = sorted([eval(packet) for packet in data if packet.strip()] + [[[2]], [[6]]], key=cmp_to_key(compare))

    a = packets.index([[2]]) + 1
    b = packets.index([[6]]) + 1

    return a * b


def main():
    print(result := part1(fileinput.input()))
    assert(result == 6568)
    print(result := part2(fileinput.input()))
    assert(result == 19493)


if __name__ == '__main__':
    main()
