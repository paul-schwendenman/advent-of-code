import fileinput
import functools
import itertools
import operator


def prod(*args: int) -> int:
    return functools.reduce(operator.mul, args)


def calculate_report(expenses, *, entry_count=2, desired_sum=2020):
    pairs = itertools.combinations(expenses, entry_count)

    for pairing in pairs:
        if sum(pairing) == desired_sum:
            break

    return prod(*pairing)


def part1(expenses):
    return calculate_report(expenses)


def part2(expenses):
    return calculate_report(expenses, entry_count=3)


def main():
    with fileinput.input() as input:
        lines = [int(line) for line in input]

    print(part1(lines))
    print(part2(lines))


if __name__ == '__main__':
    main()
