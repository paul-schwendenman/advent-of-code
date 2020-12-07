from contextlib import contextmanager
from typing import List
import fileinput


@contextmanager
def readfile(filename=None):
    with fileinput.input(filename) as data:
        yield [line.rstrip() for line in data]


def part1(data: List[str]) -> int:
    return 1


def part2(data: List[str]) -> int:
    return 2


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
