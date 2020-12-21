from __future__ import annotations
from typing import Sequence, Mapping
from itertools import product
from functools import lru_cache
from aoc import readfile, tracer, profiler
import regex


@profiler
def part1(data: Sequence[str]) -> int:
    pass


@profiler
def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
