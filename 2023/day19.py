import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing
import dataclasses
import copy

class Part(typing.NamedTuple):
    x: int
    m: int
    a: int
    s: int

class PartCategory(enum.Enum):
    pass

class Workflow(typing.NamedTuple):
    pass


def check_part(workflows, start, part):
    for rule in workflows[start]:
        match rule.get('sym'), rule["destination"]:
            case None, 'A' | 'R':
                return rule["destination"]
            case None, _:
                return check_part(workflows, rule['destination'], part)
            case ">", 'A' | 'R':
                if part[rule['var']] > rule['value']:
                    return rule["destination"]
                else:
                    continue
            case ">", _:
                if part[rule['var']] > rule['value']:
                    return check_part(workflows, rule['destination'], part)
                else:
                    continue
            case "<", 'A' | 'R':
                if part[rule['var']] < rule['value']:
                    return rule["destination"]
                else:
                    continue
            case "<", _:
                if part[rule['var']] < rule['value']:
                    return check_part(workflows, rule['destination'], part)
                else:
                    continue
            case _:
                raise ValueError("Invalid Rule", rule)


def part1(data):
    acc = 0
    workflows = {}
    while data:
        line = next(data)
        if line.strip() == '':
            break

        label, rest = line.rstrip().split('{')
        rules = []

        for rule in rest[:-1].split(','):
            try:
                condition, destination = rule.split(":")

                match = re.match(r'(?P<var>[a-z]+)(?P<sym><|>)(?P<value>[0-9]+)', condition)
                rule = match.groupdict()
                rule['value'] = int(rule['value'])
                rule['destination'] = destination

                rules.append(rule)
            except ValueError:
                rules.append({"destination": rule})


        workflows[label] = rules

    for line in data:
        part = re.match(r'\{x=(?P<x>[0-9]+),m=(?P<m>[0-9]+),a=(?P<a>[0-9]+),s=(?P<s>[0-9]+)\}', line).groupdict()
        for key in ('x', 'm', 'a', 's'):
            part[key] = int(part[key])

        if check_part(workflows, 'in', part) == 'A':
            acc += sum(part.values())



    return acc



    pass


@dataclasses.dataclass
class Area():
    x: range = range(1, 4_001)
    m: range = range(1, 4_001)
    a: range = range(1, 4_001)
    s: range = range(1, 4_001)

    def __len__(self):
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)

    def split(self, name, value):
        r = getattr(self, name)

        if r.stop < value:
            left_range, right_range = r, range(0)
        elif r.start <= value:
            left_range, right_range = range(r.start, value), range(value, r.stop)
        elif r.start > value:
            left_range, right_range = range(0), r
        # left_range, right_range = range(r.start, min(value, r.stop)), range(max(value, r.start), r.stop)
        left, right = copy.copy(self), copy.copy(self)


        setattr(left, name, left_range)
        setattr(right, name, right_range)

        assert len(left_range) + len(right_range) == len(r), f'{r}: {left} + {right}'
        # assert len(left) + len(right) == 4000 ** 4, f'{right_range}, {left_range} {len(left) + len(right)}'

        return left, right





class State(typing.NamedTuple):
    label: str
    ranges: Area


def build_solver(workflows):
    def solver(label, ranges):
        if len(ranges) == 0:
            return 0
        if label == 'A':
            return len(ranges)
        if label == 'R':
            return 0

        acc = 0
        for rule in workflows[label]:
            if 'sym' not in rule:
                acc += (s := solver(rule["destination"], ranges))
                print(f'{rule=} {s}')
            elif rule['sym'] == '>':
                ranges, here = ranges.split(rule["var"], rule['value'] + 1)

                print(f'{rule=} {ranges=} {here=}')

                acc += solver(rule["destination"], here)
            elif rule['sym'] == '<':
                here, ranges = ranges.split(rule["var"], rule['value'])

                print(f'{rule=} {here=} {ranges=}')

                acc += solver(rule["destination"], here)

        return acc
    return solver


def part2(data):
    acc = 0
    workflows = {}
    while data:
        line = next(data)
        if line.strip() == '':
            break

        label, rest = line.rstrip().split('{')
        rules = []

        for rule in rest[:-1].split(','):
            try:
                condition, destination = rule.split(":")

                match = re.match(r'(?P<var>[a-z]+)(?P<sym><|>)(?P<value>[0-9]+)', condition)
                rule = match.groupdict()
                rule['value'] = int(rule['value'])
                rule['destination'] = destination

                rules.append(rule)
            except ValueError:
                rules.append({"destination": rule})


        workflows[label] = rules

    solver = build_solver(workflows)

    ans = solver('in', Area())

    print(f'{ans / 4000 ** 4}')

    assert len(Area()) == 4000 ** 4

    return ans



    pass


def main():
    print(part1(fileinput.input()))
    print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
