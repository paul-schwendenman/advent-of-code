from __future__ import annotations
from typing import Sequence, Mapping
from itertools import product
from functools import lru_cache
from aoc import readfile, tracer, profiler
import regex


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
    value = inner(rules[rule_id])
    print(inner.cache_info())
    return value


def convert_rule(rules, rule_id):
    @lru_cache(maxsize=1000)
    # @tracer
    def inner(rule_id=None, rule=None):
        if rule is None:
            rule = rules[rule_id]
        if rule == '"a"':
            return 'a'
        elif rule == '"b"':
            return 'b'
        elif rule_id == '8':
            return f'({inner("42")})+'
        elif rule_id == '11':
            return f'(?P<eleven>{inner("42")}(?P&eleven){"{0,1}"}{inner("31")})+'
        elif '|' in rule:
            first, second = rule.split(' | ')
            return f'(({inner(rule_id, rule=first)})|({inner(rule_id, rule=second)}))'
        else:
            return ''.join(inner(rule_id=item) for item in rule.split(' '))

    print(inner.cache_info())
    value = inner(rule_id)
    print(inner.cache_info())
    return f'^{value}$'


@profiler
def part1(data: Sequence[str]) -> int:
    section_break = data.index('')
    raw_rules, messages = data[:section_break], data[section_break+1:]

    rules = parse_rules(raw_rules)

    valid_answers = set(eval_rule(rules, '0'))

    return sum(message in valid_answers for message in messages)


@profiler
def part2(data: Sequence[str]) -> int:
    section_break = data.index('')
    raw_rules, messages = data[:section_break], data[section_break+1:]

    rules = parse_rules(raw_rules)
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'

    # valid_answers = set(eval_rule(rules, '0'))
    print(convert_rule(rules, '0'))
    pattern = regex.compile(convert_rule(rules, '0'))
    print(pattern)

    return sum(1 for message in messages if regex.match(pattern, message))


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
