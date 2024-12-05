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
    print(f'update: {update}')
    for index, number in enumerate(update):
        print(f'{index}: {number} - {rules[number]} - {update[index+1:]}')
        if number in rules:
            if any(test in rules[number] for test in update[index+1:]):
                print(f'fail: {number}')
                return False
    print('valid')
    return True

    pass

def part1(data):
    lines = ''.join(line for line in data).rstrip()
    rules, updates = [chunk.split('\n') for chunk in lines.split('\n\n')]

    rules = parse_rules(rules)
    updates = parse_updates(updates)

    print(rules)

    acc = 0

    for update in updates:

        if valid(rules, update):
            middle = len(update) // 2
            acc += update[middle]
            print(update)
            print(update[middle])

    return acc





    print(updates)

    pass


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
