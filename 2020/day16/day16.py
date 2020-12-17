from __future__ import annotations
from typing import Iterator, List, MutableMapping, Set, Sequence, Optional, Tuple
from aoc import readfile
from collections import defaultdict, namedtuple
from dataclasses import dataclass
from functools import reduce
from operator import mul
import re


Notes = namedtuple('Notes', 'rules your_ticket nearby_ticket')
# Rule = namedtuple('Rule', 'field bound_1 bound_2')
Rule = Tuple[str, int, int, int, int]


def parse_notes(notes: str) -> Notes:
    top, bottom = notes.split('your ticket:')
    your_ticket, others = bottom.split('nearby tickets:')

    rules = top.strip().splitlines()
    nearby_tickets = others.strip().split('\n')

    return Notes(rules, your_ticket, nearby_tickets)


def parse_rules(rules: Iterator[str]) -> Sequence[Rule]:
    def parse(rule: str) -> Rule:
        match = re.match(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$', rule)
        if match:
            groups = match.groups()

            name = groups[0]
            bottom_lower = int(groups[1])
            bottom_upper = int(groups[2])
            top_lower = int(groups[3])
            top_upper = int(groups[4])
            # return Rule(groups[0], Range(*groups[1:2]), Range(*groups[1:2]))
            return (name, bottom_lower, bottom_upper, top_lower, top_upper)
        raise ValueError("Parse Error in rule: '%s'" % rule)
    return tuple(parse(rule) for rule in rules)


def part1(data: List[str]) -> int:
    document = '\n'.join(data)

    _, _, nearby_tickets = parse_notes(document)

    all_numbers = [int(item) for line in nearby_tickets for item in line.split(',')]

    filtered = filter(lambda a: not (25 <= a <= 973), all_numbers)

    return sum(filtered)


def part2(data: List[str]) -> int:
    document = '\n'.join(data)

    raw_rules, your_ticket, nearby_tickets = parse_notes(document)
    rules = parse_rules(raw_rules)

    all_numbers_lists = [[int(item) for item in line.split(',') if item] for line in nearby_tickets]

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
