from collections import namedtuple
from typing import List
from itertools import combinations
from aoc import readfile

Window = namedtuple('Window', 'bottom top')


def find_invalid_number(numbers: List[int], preamble_length: int = 25) -> int:
    for low_index, high_index in enumerate(range(preamble_length, len(numbers))):
        previous = [sum(pair) for pair in combinations(numbers[low_index:high_index], 2)]

        if numbers[high_index] not in previous:
            return numbers[high_index]

    raise ValueError()


def find_contiguous_set(numbers: List[int], goal: int) -> Window:
    lower_bound: int = 0
    upper_bound: int = 0
    running_total: int = 0

    while upper_bound < len(numbers):
        if running_total == goal:
            return Window(lower_bound, upper_bound)
        elif running_total < goal:
            running_total += numbers[upper_bound]
            upper_bound += 1
        else:
            running_total -= numbers[lower_bound]
            lower_bound += 1

    raise ValueError()


def part1(data: List[str]) -> int:
    numbers = [int(num) for num in data]

    return find_invalid_number(numbers, 25)


def part2(data: List[str], goal: int) -> int:
    numbers = [int(num) for num in data]

    window = find_contiguous_set(numbers, goal)

    weak_range = numbers[window.bottom:window.top]

    return min(weak_range) + max(weak_range)


def main() -> None:
    with readfile() as data:
        part1_solution = part1(data)
        print(part1_solution)
        print(part2(data, part1_solution))


if __name__ == '__main__':
    main()
