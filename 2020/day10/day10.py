from typing import List
from collections import defaultdict
from aoc import readfile


# def next_adapter():


def part1(data: List[str]) -> int:
    adapters = [0] + sorted([int(item) for item in data])

    counts = defaultdict(int)

    for index, adapter in enumerate(adapters[:-1]):
        counts[adapters[index+1] - adapter] += 1

    return counts[1] * (counts[3] + 1)


def arrangements(adapters, base, goal):
    if base == goal:
        return 1
    if base not in adapters:
        return 0

    return arrangements(adapters, base+1, goal) + arrangements(adapters, base+2, goal) + arrangements(adapters, base+3, goal)


def part2_slow(data: List[str]) -> int:
    adapters = [0] + sorted([int(item) for item in data])

    goal = max(adapters) + 3

    return arrangements(adapters, 0, goal)


def part2(data: List[str]) -> int:
    adapters = [0] + sorted([int(item) for item in data])

    adapters.append(adapters[-1] + 3)

    small = []
    ways = 1

    for index, adapter in enumerate(adapters[:-1]):
        if adapters[index+1] - adapter == 3:
            small.append(adapter)
            ways *= arrangements(small, small[0], small[-1])
            small = [adapter]
        else:
            small.append(adapter)

    return ways


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
