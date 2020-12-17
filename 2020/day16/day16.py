from __future__ import annotations
from typing import List, MutableMapping, Set
from aoc import readfile
from collections import defaultdict
from functools import reduce
from operator import add, mul


def part1(data: List[str]) -> int:
    document = '\n'.join(data)
    top, bottom = document.split('your ticket:')
    your_ticket, others = bottom.split('nearby tickets:')

    nearby_tickets = others.strip().split('\n')
    # print(nearby_tickets[0:5])

    all_numbers_lists = [[int(item) for item in line.split(',') if item] for line in others.split('\n')]
    # print(all_numbers[0:30])
    all_numbers = sorted(reduce(add, all_numbers_lists))

    filtered = filter(lambda a: not (25 <= a <= 973), all_numbers)

    return sum(filtered)


# /(.*): (\d+)-(\d+) or (\d+)-(\d+)/
rules = (
    ("departure location", 32, 69, 86, 968),
    ("departure station", 27, 290, 301, 952),
    ("departure platform", 47, 330, 347, 956),
    ("departure track", 46, 804, 826, 956),
    ("departure date", 25, 302, 320, 959),
    ("departure time", 29, 885, 893, 961),
    ("arrival location", 33, 643, 649, 963),
    ("arrival station", 29, 135, 151, 973),
    ("arrival platform", 50, 648, 674, 961),
    ("arrival track", 45, 761, 767, 971),
    ("class", 46, 703, 725, 951),
    ("duration", 47, 244, 257, 957),
    ("price", 49, 195, 209, 956),
    ("route", 44, 368, 393, 968),
    ("row", 48, 778, 797, 954),
    ("seat", 31, 421, 427, 964),
    ("train", 42, 229, 245, 961),
    ("type", 31, 261, 281, 964),
    ("wagon", 36, 428, 445, 967),
    ("zone", 30, 906, 923, 960),)


def part2(data: List[str]) -> int:
    document = '\n'.join(data)
    top, bottom = document.split('your ticket:')
    your_ticket, others = bottom.split('nearby tickets:')

    nearby_tickets = others.strip().split('\n')

    all_numbers_lists = [[int(item) for item in line.split(',') if item] for line in others.split('\n')]

    filtered = [item for item in filter(lambda l: all((25 <= a <= 973) for a in l), all_numbers_lists) if item]

    filtered.append([int(i) for i in your_ticket.split(',')])

    rotated = list(zip(*filtered))

    field_option_set = defaultdict(set)

    for index, line in enumerate(rotated):
        for rule in rules:
            if all(map(lambda num: (rule[1] <= num <= rule[2] or rule[3] <= num <= rule[4]), line)):
                field_option_set[index].add(rule[0])

    field_options: MutableMapping[str, int] = {}
    used_fields: Set[str] = set()

    for item in sorted(field_option_set.items(), key=lambda pair: len(pair[1])):
        leftover = (item[1] - used_fields).pop()
        field_options[leftover] = item[0]
        used_fields.add(leftover)

    fields = set(value for key, value in field_options.items() if 'departure' in key)

    return reduce(mul, [int(value) for index, value in enumerate(your_ticket.split(',')) if index in fields])


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
