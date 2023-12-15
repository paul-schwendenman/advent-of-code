import fileinput
import re
import itertools
import math
import functools
import collections
import enum

def holiday_hash(str):
    value = 0
    for chr in str:
        value += ord(chr)
        value *= 17
        value = value % 256

    return value


def part1(data):
    line = next(data).strip()
    parts = line.split(',')

    return sum(holiday_hash(part) for part in parts)

    pass


def part2(data):
    line = next(data)
    boxes: dict[int, dict] = collections.defaultdict(dict)
    parts = line.split(',')
    # print(f'{parts=}')
    focusing_power = 0

    for part in parts:
        match = re.match(f'([A-Za-z]+)(=|-)([0-9]*)', part)
        if not match:
            raise ValueError

        label, op, focal_length = match.groups()
        try:
            focal_length = int(focal_length)
        except ValueError:
            focal_length = None
        box_index = holiday_hash(label)

        if op == '=':
            if label in boxes[box_index]:
                boxes[box_index][label] = focal_length
            else:
                boxes[box_index][label] = focal_length

        elif op == '-' and label in boxes[box_index]:
            del(boxes[box_index][label])

        # print(dict(boxes))


    focusing_power = 0


    for idx in (1 + i for i in sorted(boxes.keys())):
        for i, strength in enumerate(boxes[idx - 1].values(), start=1):
            focusing_power += idx * i * strength




    return focusing_power
    pass


def main():
    data = list(line.strip() for line in fileinput.input())
    print(part1(iter(data)))
    print(part2(iter(data)))


if __name__ == '__main__':
    main()
