import fileinput
from dataclasses import dataclass, field
from types import FunctionType
from typing import TypeVar
from collections import deque
from collections.abc import Sequence, Iterator, Iterable, Callable
import math
import re

Item = TypeVar('Item')


def chunk(array: Sequence[Item], size=1) -> Iterator[Sequence[Item]]:
    for i in range(0, len(array), size):
        yield array[i:i+size]


@dataclass
class Monkey:
    id: int
    operation: Callable[[int], int]
    test: int
    yes: int
    no: int
    items: deque = field(default_factory=deque)
    inspections: int = field(default = 0, init=False)

    def add(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.popleft()
        except IndexError:
            return None

    def test_item(self, item):
        return item % self.test == 0

    def inspect(self, item):
        self.inspections += 1
        return self.operation(item)

    def pass_item(self, monkeys, item):
        if self.test_item(item):
            return monkeys[self.yes].add(item)
        else:
            return monkeys[self.no].add(item)


def extract_ints(line: str) -> Sequence[int]:
    return list(map(int, re.findall(r'-?[0-9]+', line)))


def parse_operation(line: str) -> Callable[[int], int]:
    _, new, eq, old, op, value = line.strip().split(" ")
    assert new == 'new'
    assert eq == '='
    assert old == 'old'

    if value == 'old':
        return lambda num: num * num

    if op == '*':
        return lambda num: num * int(value)
    elif op == '+':
        return lambda num: num + int(value)
    else:
        raise ValueError("Invalid op '%s'", op)


def parse_monkey(raw_monkey: Sequence[str]) -> Monkey:
    id = extract_ints(raw_monkey[0])[0]
    items = deque(extract_ints(raw_monkey[1]))
    operation = parse_operation(raw_monkey[2])
    test = extract_ints(raw_monkey[3])[0]
    yes = extract_ints(raw_monkey[4])[0]
    no = extract_ints(raw_monkey[5])[0]

    return Monkey(id, operation, test, yes, no, items)


def parse_monkeys(data) -> Iterable[Monkey]:
    monkeys = []
    for raw_monkey in chunk(list(data), 7):
        monkeys.append(parse_monkey(raw_monkey))

    return monkeys


def part1(data):
    monkeys:Iterable[Monkey] = parse_monkeys(data)

    for round in range(20):
        for monkey in monkeys:
            while item := monkey.pop():
                new = monkey.inspect(item)

                relief = new // 3

                monkey.pass_item(monkeys, relief)

    inspections = sorted([monkey.inspections for monkey in monkeys])

    return math.prod(inspections[-2:])


def part2(data):
    monkeys:Iterable[Monkey] = parse_monkeys(data)

    max_worry = math.prod(monkey.test for monkey in monkeys)

    for round in range(10_000):
        for monkey in monkeys:
            while item := monkey.pop():
                new = monkey.inspect(item)

                relief = new % max_worry

                monkey.pass_item(monkeys, relief)

    inspections = sorted([monkey.inspections for monkey in monkeys])

    # return inspections[-1] * inspections[-2]
    return math.prod(inspections[-2:])


def main():
    print(part1(fileinput.input()))
    assert(part1(fileinput.input()) == 50172)
    print(part2(fileinput.input()))
    assert(part2(fileinput.input()) == 11614682178)


if __name__ == '__main__':
    main()
