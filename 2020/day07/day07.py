from contextlib import contextmanager
from collections import defaultdict
from functools import reduce
from typing import List
import fileinput


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


def strip_quanity(raw_bag):
    return raw_bag.split(' ', 1)[1]


def strip_bags(raw_bag):
    return raw_bag.strip().replace('bags', 'bag')


def parse_rule(raw_rule):
    parent, raw_children = raw_rule[:-1].split('contain')

    children = [strip_bags(child) for child in raw_children.split(',')]

    if children == ["no other bag"]:
        return None

    return strip_bags(parent), children

def search(item, tree):
    if item not in tree:
        return set()

    return reduce(set.union, (search(parent, tree) for parent in tree[item]), set(tree[item]))


def part1(data: List[str]) -> int:
    rules = defaultdict(list)
    for raw_rule in data:
        rule = parse_rule(raw_rule)

        if rule:
            # print(rule)
            parent, children = rule

            for child in children:
                # print(strip_quanity(child))
                rules[strip_quanity(child)].append(parent)

    # print(rules.keys())
    # print(len(rules['shiny gold bag']))

    count = 0

    return len(search('shiny gold bag', rules))


def part2(data: List[str]) -> int:
    return 2


def main() -> None:
    with readfile() as data:
        print(part1(data))
        # print(part2(data))


if __name__ == '__main__':
    main()
