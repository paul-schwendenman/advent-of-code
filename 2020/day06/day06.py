from contextlib import contextmanager
from functools import reduce
from typing import List
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


def part1(groups: List[str]) -> int:
    count = 0

    for group in groups:
        answers = set()
        for person in group.split('\n'):
            for answer in person:
                answers.add(answer)
        count += len(answers)

    return count


def part2(groups: List[str]) -> int:
    count = 0

    for group in groups:
        answers = [set(person) for person in group.split('\n') if person]

        count += len(reduce(set.intersection, answers))

    return count


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
