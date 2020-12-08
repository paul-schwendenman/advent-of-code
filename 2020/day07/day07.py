from contextlib import contextmanager
from typing import Dict, List, Tuple
import fileinput
import re


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


Rules = Dict[str, Dict[str, int]]


def strip_bags(raw_bag: str) -> str:
    return raw_bag.replace('bags', '').replace('bag', '').strip()


def parse_quanity(raw_bag: str) -> Tuple[str, int]:
    match = re.match(r'.*?([0-9]+) (.+?) bags?', raw_bag)

    if not match:
        raise ValueError("No match")

    count, bag = match.groups()

    return strip_bags(bag), int(count)


def parse_rules(raw_rules: List[str]) -> Rules:
    rules: Rules = {}
    for rule in raw_rules:
        raw_parent, raw_children = rule[:-1].split('contain')

        if 'no other bag' in raw_children:
            continue

        parent = strip_bags(raw_parent)

        children = [parse_quanity(child) for child in raw_children.split(',')]

        rules[parent] = dict(children)

    return rules


def count_bags(rules: Rules, parent: str, quanity: int) -> int:
    if parent not in rules:
        return quanity

    return quanity * (1 + sum(count_bags(rules, child, child_quanity) for child, child_quanity in rules[parent].items()))


def bag_contains(rules: Rules, bag: str, target: str) -> bool:
    if bag not in rules:
        return False

    return target in rules[bag] or any(bag_contains(rules, parent, target) for parent in rules[bag])


def part1(data: List[str], target: str = 'shiny gold') -> int:
    rules = parse_rules(data)

    return sum(bag_contains(rules, key, target) for key in rules.keys())


def part2(data: List[str]) -> int:
    rules = parse_rules(data)

    return count_bags(rules, 'shiny gold', 1) - 1


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
