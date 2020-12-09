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


def part2(data: List[str], goal=556543474) -> int:
    numbers = [int(num) for num in data]
    bounds = None

    for index, number in enumerate(numbers):
        pos = index
        sum = 0
        while sum < goal and pos < len(numbers):
            sum += numbers[pos]
            pos += 1

        if sum == goal:
            bounds = (index, pos)
            break
    else:
        raise ValueError()

    weak_range = numbers[bounds[0]:bounds[1]]

    return min(weak_range) + max(weak_range)


def main() -> None:
    with readfile() as data:
        # print(part1(data, 25))
        # print(part2(data, 127))
        print(part2(data))


if __name__ == '__main__':
    main()
