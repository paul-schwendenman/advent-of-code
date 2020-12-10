from typing import Iterator, List, Tuple
from collections import defaultdict
from itertools import islice
from aoc import readfile


def generate_pairs(seq: List[int]) -> Iterator[Tuple[int, int]]:
    yield from zip(seq, islice(seq, 1, None))


def tribonacci(n: int, n_0: int = 0, n_1: int = 0, n_2: int = 1) -> int:
    '''Tribonacci sequence

    0, 0, 1, 1, 2, 4, 7, 13...
    '''
    if n == 0:
        return n_0
    elif n == 1:
        return n_1
    elif n == 2:
        return n_2
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


def part1(data: List[str]) -> int:
    adapters = [0] + sorted([int(item) for item in data])

    counts = defaultdict(int)

    for index, adapter in enumerate(adapters[:-1]):
        counts[adapters[index+1] - adapter] += 1

    return counts[1] * (counts[3] + 1)


def part2(data: List[str]) -> int:
    adapters = [0] + sorted([int(item) for item in data])
    adapters.append(adapters[-1] + 3)

    arrangements = 1
    count = 0

    for adapter, next_adapter in generate_pairs(adapters):
        if next_adapter - adapter == 3:
            arrangements *= tribonacci(count + 2)
            count = 0
        else:
            count += 1

    return arrangements


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
