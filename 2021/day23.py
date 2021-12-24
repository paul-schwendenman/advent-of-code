import fileinput
from itertools import cycle, product
from collections import Counter, namedtuple
from typing import MutableMapping, Tuple
from enum import Enum


def part1(data: list[str]) -> int:
    pass


def part2(data: list[str]) -> int:
    pass


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
