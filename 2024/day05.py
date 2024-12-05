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


def parse_rules2(rules):
    pairs = []
    for rule in rules:
        before, after = map(int, rule.split('|'))

        pairs.append((before, after))


    return pairs


def parse_updates(updates):
    return [extract_ints(update) for update in updates]


def valid(rules, update):
    # print(f'update: {update}')
    for index, number in enumerate(update):
        # print(f'{index}: {number} - {rules[number]} - {update[index+1:]}')
        if number in rules:
            if any(test in rules[number] for test in update[index+1:]):
                # print(f'fail: {number}')
                return False
    # print('valid')
    return True

    pass

def part1(data):
    lines = ''.join(line for line in data).rstrip()
    rules, updates = [chunk.split('\n') for chunk in lines.split('\n\n')]

    rules = parse_rules(rules)
    updates = parse_updates(updates)

    # print(rules)

    acc = 0

    for update in updates:

        if valid(rules, update):
            middle = len(update) // 2
            acc += update[middle]
            # print(update)
            # print(update[middle])

    return acc


def sort_update(update, rules):
    update = update[:]
    sorted_update = [update.pop()]

    while len(update) > 0:
        print(f'len(update)={len(update)} - {update} - {sorted_update}')
        number = update.pop()

        if any(test in rules[number] for test in sorted_update):
            sorted_update = sorted_update + [number]
        # if all(test in rules[number] for test in sorted_update):
        else:
            sorted_update = [number] + sorted_update



    return sorted_update


def part2(data):
    lines = ''.join(line for line in data).rstrip()
    rules, updates = [chunk.split('\n') for chunk in lines.split('\n\n')]

    rules2 = parse_rules2(rules)
    rules = parse_rules(rules)
    updates = parse_updates(updates)

    # print(rules)

    acc = 0

    def compare(a, b):
        if (a, b) in rules2:
            return -1

        return 1


    for update in updates:

        if not valid(rules, update):
            # print(update)
            # sorted_update = sort_update(update, rules)
            sorted_update = sorted(update, key=functools.cmp_to_key(compare))
            # print(sorted_update)
            middle = len(sorted_update) // 2
            acc += sorted_update[middle]


    return acc
    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
