from __future__ import annotations
from typing import Sequence, Mapping
from itertools import product
from functools import lru_cache
from aoc import readfile, tracer, profiler


def parse_rules(rules: Sequence[str]) -> Mapping[str, str]:
    mapping = {}

    for rule in rules:
        key, value = rule.split(': ')
        mapping[key] = value
    return mapping


# @tracer
def eval_rule(rules, rule_id):
    @lru_cache(maxsize=1000)
    # @tracer
    def inner(rule):
        if rule == '"a"':
            return ['a']
        elif rule == '"b"':
            return ['b']
        elif '|' in rule:
            first, second = rule.split(' | ')
            return [item for group in (inner(first), inner(second)) for item in group]
        else:
            return list(''.join(item) for item in product(*[inner(rules[item]) for item in rule.split(' ')]))

    print(inner.cache_info())
    value =  inner(rules[rule_id])
    print(inner.cache_info())
    return value


@profiler
def part1(data: Sequence[str]) -> int:
    section_break = data.index('')
    raw_rules, messages = data[:section_break], data[section_break+1:]

    rules = parse_rules(raw_rules)

    valid_answers = set(eval_rule(rules, '0'))

    return sum(message in valid_answers for message in messages)

    # print(list(valid_answers))


def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
