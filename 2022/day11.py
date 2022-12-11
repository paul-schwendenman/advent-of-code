import fileinput
from dataclasses import dataclass, field
from types import FunctionType
import math
from copy import copy, deepcopy


@dataclass
class Monkey:
    id: int
    operation: FunctionType
    test: int
    yes: int
    no: int
    items: list = field(default_factory=list)
    inspections: int = 0


sample_monkeys = [
    Monkey(
        id=0,
        operation =lambda a: a * 19,
        test = 23,
        yes = 2,
        no = 3,
        items = [79, 98]
    ),
    Monkey(
        id=1,
        operation =lambda a: a + 6,
        test = 19,
        yes = 2,
        no = 0,
        items = [54, 65, 75, 74]
    ),
    Monkey(
        id=2,
        operation =lambda a: a * a,
        test = 13,
        yes = 1,
        no = 3,
        items = [79, 60, 97]
    ),
    Monkey(
        id=3,
        operation =lambda a: a + 3,
        test = 17,
        yes = 0,
        no = 1,
        items = [74]
    ),
]

monkeys2 = [
    Monkey(
        id=0,
        operation =lambda a: a * 7,
        test = 17,
        yes = 5,
        no = 3,
        items = [54, 61, 97, 63, 74]
    ),
    Monkey(
        id=1,
        operation =lambda a: a + 8,
        test = 2,
        yes = 7,
        no = 6,
        items = [61, 70, 97, 64, 99, 83, 52, 87]
    ),
    Monkey(
        id=2,
        operation =lambda a: a * 13,
        test = 5,
        yes = 1,
        no = 6,
        items = [60, 67, 80, 65]
    ),
    Monkey(
        id=3,
        operation =lambda a: a + 7,
        test = 3,
        yes = 5,
        no = 2,
        items = [61, 70, 76, 69, 82, 56]
    ),
    Monkey(
        id=4,
        operation =lambda a: a + 2,
        test = 7,
        yes = 0,
        no = 3,
        items = [79, 98]
    ),
    Monkey(
        id=5,
        operation =lambda a: a + 1,
        test = 13,
        yes = 2,
        no = 1,
        items = [72, 79, 55]
    ),
    Monkey(
        id=6,
        operation =lambda a: a + 4,
        test = 19,
        yes = 7,
        no = 4,
        items = [63]
    ),
    Monkey(
        id=7,
        operation =lambda a: a * a,
        test = 11,
        yes = 0,
        no = 4,
        items = [72, 51, 93, 63, 80, 86, 81]
    ),
]


def parse_monkey():
    pass


def parse_monkeys():
    pass


def part1(data):
    # monkeys = deepcopy(sample_monkeys)
    monkeys = deepcopy(monkeys2)
    for round in range(20):
        print(f'------------ round {round + 1}')
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
    pass
    inspections = sorted([monkey.inspections for monkey in monkeys])
    print(inspections)
    for monkey in monkeys:
        print(f"monkey {monkey.id}: {monkey.items}")

    return inspections[-1] * inspections[-2]



def part2(data):
    # monkeys = sample_monkeys.copy()
    monkeys = deepcopy(monkeys2)
    print(0, [monkey.inspections for monkey in monkeys])
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

        if (round + 1) in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            print(round+1, [monkey.inspections for monkey in monkeys])
    pass
    inspections = sorted([monkey.inspections for monkey in monkeys])
    print(inspections)

    return inspections[-1] * inspections[-2]
    pass


def main():
    print(part1(fileinput.input()))
    assert(part1(fileinput.input()) == 50172)
    print(part2(fileinput.input()))
    assert(part2(fileinput.input()) == 11614682178)


if __name__ == '__main__':
    main()
