from typing import List
import fileinput
import functools
import itertools
import operator


def prod(*args: int) -> int:
    return functools.reduce(operator.mul, args)


def calculate_report(expenses: List[int], *, entry_count: int = 2, desired_sum: int = 2020) -> int:
    pairs = itertools.combinations(expenses, entry_count)

    for pairing in pairs:
        if sum(pairing) == desired_sum:
            break

    return prod(*pairing)


def part1(expenses: List[int]) -> int:
    return calculate_report(expenses)


def part2(expenses: List[int]) -> int:
    return calculate_report(expenses, entry_count=3)


def main() -> None:
    with fileinput.input() as input:
        lines = [int(line) for line in input]

    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
