from __future__ import annotations
from typing import List
from aoc import readfile
from collections import defaultdict, Counter


def part1(data: str, turns: int = 2020) -> int:
    start = [int(num) for num in data.split(',')]
    counter = defaultdict(list)

    turn = 0

    for item in start:
        turn += 1
        counter[item].append(turn)

    last_num = item

    while turn < turns:
        if len(counter[last_num]) == 1:
            last_num = 0
        else:
            second_last, last = counter[last_num][-2:]
            print(f'{last} - {second_last} = {last - second_last}')
            last_num = last - second_last

        turn += 1
        counter[last_num].append(turn)
        print(turn, last_num)

    return last_num


def part2(data: List[str]) -> int:
    pass


def main() -> None:
    print(part1("6,3,15,13,1,0"))
    # print(part1(data))


if __name__ == '__main__':
    main()
