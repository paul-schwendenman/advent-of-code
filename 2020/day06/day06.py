from contextlib import contextmanager
from functools import reduce
from typing import Callable, Iterable, List
import sys


@contextmanager
def readfile(filename=None):
    if not filename:
        try:
            filename = sys.argv[1]
        except IndexError:
            filename = 0

    with open(filename) as data:
        yield data.read().split('\n\n')


def parse_answers(group: str) -> Iterable[set]:
    return (set(person) for person in group.split('\n') if person)


def solve(groups: List[str], func: Callable[[set, set], set]) -> int:
    return sum(len(reduce(func, parse_answers(group))) for group in groups)


def part1(groups: List[str]) -> int:
    return solve(groups, set.union)


def part2(groups: List[str]) -> int:
    return solve(groups, set.intersection)


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
