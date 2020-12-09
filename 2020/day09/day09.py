from typing import List
from itertools import combinations
from aoc import readfile


def part1(data: List[str], preamble: int = 25) -> int:
    numbers = [int(num) for num in data]

    for index, num in enumerate(range(preamble, len(numbers))):
        print((index - preamble), numbers[index:num])
        previous = [sum(pair) for pair in combinations(numbers[(index):num], 2)]

        print(index, num, previous)

        if numbers[num] not in previous:
            return numbers[num]

    raise ValueError()


def part2(data: List[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data, 25))
        print(part2(data))


if __name__ == '__main__':
    main()
