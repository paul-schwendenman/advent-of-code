from __future__ import annotations
from typing import Sequence, Deque, Tuple
from aoc import readfile
from collections import deque


def part1(raw_cups: str, rounds=100) -> str:
    cups = deque(map(int, list(raw_cups)))

    for move in range(rounds):
        print(f'------ move {move+1} -----')
        print(f'cups: {" ".join(f"({cup})" if index % 9 == move else f" {cup} " for index, cup in enumerate(cups))}')
        cups.rotate(-move)
        current = cups.popleft()
        burn_1 = cups.popleft()
        burn_2 = cups.popleft()
        burn_3 = cups.popleft()
        print(f'pick up: {", ".join(map(str, [burn_1, burn_2, burn_3]))}')
        destination = (current - 1) % 9 if current != 1 else 9
        while destination not in cups:
            destination = (destination - 1) % 9 if destination != 1 else 9
        print(f'destination: {destination}')

        print(f'current: {current}')

        print(cups)
        offset = -(cups.index(destination))
        cups.rotate(offset)
        print(cups, offset, "rotate")
        destination_cup = cups.popleft()
        assert destination_cup == destination
        print(cups, f"removed {destination_cup}")
        cups.extendleft([burn_3, burn_2, burn_1, destination_cup])
        print(cups, "extend")
        cups.rotate(-offset)
        print(cups, f"rotated {-offset}")
        cups.appendleft(current)
        print(cups, "append")
        cups.rotate(move)
        print(cups, "final")


    print('-- final --')
    print(f'cups: {" ".join(f" {cup} " for cup in cups)}')
    offset = cups.index(1)
    cups.rotate(-(offset + 1))
    # print(cups)
    cups.pop()
    # print(cups)

    return ''.join(map(str, cups))


def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    # with readfile() as data:
    #     pass
    print(part1("389125467", 10))
    print(part1("389125467", 100))
    print(part1("784235916", 100))
    # print(part1(data))
    # print(part2(data))


if __name__ == '__main__':
    main()
