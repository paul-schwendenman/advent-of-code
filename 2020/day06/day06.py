from contextlib import contextmanager
from typing import List
import fileinput
import functools


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield ''.join(data).split('\n\n')


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

        count += len(functools.reduce(set.intersection, answers))

    return count


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
