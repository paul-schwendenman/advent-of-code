import fileinput
from dataclasses import dataclass, field
from types import FunctionType
import math
import re


def chunk(array, size=1):
    for i in range(0, len(array), size):
        yield array[i:i+size]


@dataclass
class Monkey:
    id: int
    operation: FunctionType
    test: int
    yes: int
    no: int
    items: list = field(default_factory=list)
    inspections: int = 0


def extract_ints(line):
    return list(map(int, re.findall(r'-?[0-9]+', line)))


def parse_operation(line):
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


def parse_monkey(raw_monkey):
    id = extract_ints(raw_monkey[0])[0]
    items = extract_ints(raw_monkey[1])
    operation = parse_operation(raw_monkey[2])
    test = extract_ints(raw_monkey[3])[0]
    yes = extract_ints(raw_monkey[4])[0]
    no = extract_ints(raw_monkey[5])[0]

    return Monkey(id, operation, test, yes, no, items)


def parse_monkeys(data):
    monkeys = []
    for raw_monkey in chunk(list(data), 7):
        monkeys.append(parse_monkey(raw_monkey))

    return monkeys


def part1(data):
    monkeys = parse_monkeys(data)

    for round in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                new = monkey.operation(item)
                relief = new // 3
                if relief % monkey.test == 0:
                    monkeys[monkey.yes].items.append(relief)
                else:
                    monkeys[monkey.no].items.append(relief)
            monkey.items = []

    inspections = sorted([monkey.inspections for monkey in monkeys])

    return inspections[-1] * inspections[-2]



def part2(data):
    monkeys = parse_monkeys(data)

    max_worry = math.prod(monkey.test for monkey in monkeys)
    for round in range(10_000):
        # print(f'------------ round {round + 1}')
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                new = monkey.operation(item)
                relief = new % max_worry
                if relief % monkey.test == 0:
                    monkeys[monkey.yes].items.append(relief)
                else:
                    monkeys[monkey.no].items.append(relief)
            monkey.items = []

    inspections = sorted([monkey.inspections for monkey in monkeys])

    return inspections[-1] * inspections[-2]


def main():
    print(part1(fileinput.input()))
    assert(part1(fileinput.input()) == 50172)
    print(part2(fileinput.input()))
    assert(part2(fileinput.input()) == 11614682178)


if __name__ == '__main__':
    main()
