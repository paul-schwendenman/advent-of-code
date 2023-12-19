import fileinput
import re
import itertools
import math
import functools
import collections
import enum
import pprint
import typing

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


def part2(data):
    pass


def main():
    print(part1(fileinput.input()))
    # print(part2(fileinput.input()))


if __name__ == '__main__':
    main()
