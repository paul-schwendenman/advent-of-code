from contextlib import contextmanager
from typing import List
import fileinput
import functools


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line for line in data]


def part1(data: List[str]) -> int:
    count = 0
    groups = ''.join(data).split('\n\n')

    for group in groups:
        questions = set()
        for person in group.split('\n'):
            for question in person:
                questions.add(question)
        count += len(questions)

    return count


def part2(data: List[str]) -> int:
    count = 0
    groups = ''.join(data).split('\n\n')

    for group in groups:
        answers = [set(item) for item in group.split('\n') if item]

        count += len(functools.reduce(set.intersection, answers))

    return count


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
