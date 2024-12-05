import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing


def extract_ints(string):
    return list(map(int, re.findall(r'-?\d+', string)))


def parse_rules(rules):
    mapping = collections.defaultdict(list)

    for rule in rules:
        before, after = map(int, rule.split('|'))

        mapping[after].append(before)

    return mapping


def parse_updates(updates):
    return [extract_ints(update) for update in updates]


def valid(rules, update):
    for index, number in enumerate(update):
        if number in rules:
            if any(test in rules[number] for test in update[index+1:]):
                return False
    return True

    pass

def part1(data):
    lines = ''.join(line for line in data).rstrip()
    rules, updates = [chunk.split('\n') for chunk in lines.split('\n\n')]

    rules = parse_rules(rules)
    updates = parse_updates(updates)

    acc = 0

    for update in updates:

        if valid(rules, update):
            middle = len(update) // 2
            acc += update[middle]

    return acc


def part2(data):
    lines = ''.join(line for line in data).rstrip()
    rules, updates = [chunk.split('\n') for chunk in lines.split('\n\n')]

    rules = parse_rules(rules)
    updates = parse_updates(updates)

    acc = 0

    def compare(a, b):
        if b in rules[a]:
            return -1

        return 1


    for update in updates:

        if not valid(rules, update):
            sorted_update = sorted(update, key=functools.cmp_to_key(compare))

            middle = len(sorted_update) // 2
            acc += sorted_update[middle]

    return acc


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
