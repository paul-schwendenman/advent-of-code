import fileinput
import json
from functools import cmp_to_key


def compare(a, b):
    types = type(a), type(b)
    # print(a, b, types)

    if types == (int, int):
        if a < b:
            return 1
        elif a > b:
            return -1
        return 0
    elif types == (list, int):
        return compare(a, [b])
    elif types == (int, list):
        return compare([a], b)
    elif types == (list, list):
        for i in range(max(len(a), len(b))):
            if len(a) <= i:
                return 1
            elif len(b) <= i:
                return -1
            else:
                if (result := compare(a[i], b[i])) == 0:
                    continue
                return result
        else:
            return 0
    else:
        raise ValueError("Types: %s", types)


def part1(data):
    pairs = (tuple(eval(pairing.strip()) for pairing in pair.split('\n')) for pair in ''.join(data).strip().split('\n\n'))
    count = 0
    correct_pairs = []

    for i, pair in enumerate(pairs):
        if (compare(*pair) != -1):
            count += 1
            correct_pairs.append(i)

    return sum(correct_pairs) + len(correct_pairs)


def part2(data):
    packets = sorted([eval(packet) for packet in data if packet.strip()] + [[[2]], [[6]]], key=cmp_to_key(compare), reverse=True)

    a = packets.index([[2]]) + 1
    b = packets.index([[6]]) + 1

    # print(a, b)

    # a = sum(1 for packet in packets if 1 == compare(packet, [[2]])) + 1
    # b = sum(1 for packet in packets if 1 == compare(packet, [[6]])) + 1

    # print(a, b)
    # print(packets)

    return a * b


def main():
    print(result := part1(fileinput.input()))
    assert(result == 6568)
    print(result := part2(fileinput.input()))
    assert(result == 19493)


if __name__ == '__main__':
    main()
