from __future__ import annotations
from typing import Sequence, Mapping
from itertools import zip_longest, islice
# from aoc import readfile
# from collections import deque, namedtuple
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    pointer: int


class LinkedList:
    def __init__(self, initial_data: Sequence[int], /, current: int = None, *, circular: bool = False):
        self._data: Mapping[int, Node] = {
            item: Node(item, next_item) for item, next_item in zip_longest(initial_data, initial_data[1:])}

        if current:
            self._current = current
        else:
            self._current = initial_data[0]

        if circular:
            self._data[initial_data[-1]].pointer = initial_data[0]

    @property
    def current(self):
        return self._data[self._current]

    @current.setter
    def current(self, current):
        self._current = current

    def __iter__(self):
        active = self.current
        start = active.value

        while True:
            yield active
            active = self._data[active.pointer]

            if active.value == start or active.pointer is None:
                break

    def __str__(self):
        return ' '.join(map(str, (node.value for node in self)))

    def __len__(self):
        return len(self._data.keys())

    def __getitem__(self, key):
        if isinstance(key, slice):
            raise NotImplementedError
        elif isinstance(key, int):
            if key < 0:
                raise NotImplementedError
            return self._data[key]
        else:
            raise TypeError("Invalid argument type.")


def get_destination(current: int, _max: int, values: Sequence[int]) -> int:
    dest = ((current - 1) % _max) or _max
    if dest in values:
        return get_destination(dest, _max, values)

    return dest


def part1(raw_cups: str, rounds: int = 100) -> str:
    cups = LinkedList([int(cup) for cup in raw_cups], circular=True)

    for move in range(rounds):
        print(f'------ move {move+1} -----')
        # print(f'cups: {" ".join(f"({cup.value})" if index % 9 == move else f" {cup.value} " for index, cup in enumerate(cups))}')
        print(f'cups: {cups}')
        # cups.rotate(-move)
        current = cups.current
        # Remove cups
        burn_1 = cups[current.pointer]
        burn_2 = cups[burn_1.pointer]
        burn_3 = cups[burn_2.pointer]
        current.pointer = burn_3.pointer
        print(f'pick up: {", ".join(map(lambda cup: str(cup.value), [burn_1, burn_2, burn_3]))}')
        destination = get_destination(current.value, len(cups), [cup.value for cup in (burn_1, burn_2, burn_3)])
        print(f'destination: {destination}')

        # Insert cups
        destination_cup = cups[destination]
        next_cup = destination_cup.pointer
        destination_cup.pointer = burn_1.value
        burn_3.pointer = next_cup

        cups.current = current.pointer


        # print(f'current: {current}')

        # print(cups)
        # offset = -(cups.index(destination))
        # cups.rotate(offset)
        # print(cups, offset, "rotate")
        # destination_cup = cups.popleft()
        # assert destination_cup == destination
        # print(cups, f"removed {destination_cup}")
        # cups.extendleft([burn_3, burn_2, burn_1, destination_cup])
        # print(cups, "extend")
        # cups.rotate(-offset)
        # print(cups, f"rotated {-offset}")
        # cups.appendleft(current)
        # print(cups, "append")
        # cups.rotate(move)
        # print(cups, "final")


    print('-- final --')
    # print(f'cups: {" ".join(f" {cup} " for cup in cups)}')
    # offset = cups.index(1)
    # cups.rotate(-(offset + 1))
    # print(cups)
    # cups.pop()
    cups.current = 1
    # print(cups)

    return ''.join(str(cup.value) for cup in islice(cups, 1, None))


def part2(raw_cups: Sequence[str], rounds=100) -> int:
    cups = deque(map(int, list(raw_cups)))

    for index in range(10, 1_000_001):
        cups.append(index)

    for move in range(rounds):
        if move % 1_000 == 0:
            print(f'------ move {move+1} -----')
        # print(f'cups: {" ".join(f"({cup})" if index % 9 == move else f" {cup} " for index, cup in enumerate(cups))}')
        cups.rotate(-move)
        current = cups.popleft()
        burn_1 = cups.popleft()
        burn_2 = cups.popleft()
        burn_3 = cups.popleft()
        # print(f'pick up: {", ".join(map(str, [burn_1, burn_2, burn_3]))}')
        destination = (current - 1) % 9 if current != 1 else 9
        while destination not in cups:
            destination = (destination - 1) % 9 if destination != 1 else 9
        # print(f'destination: {destination}')

        # print(f'current: {current}')

        # print(cups)
        offset = -(cups.index(destination))
        cups.rotate(offset)
        # print(cups, offset, "rotate")
        destination_cup = cups.popleft()
        assert destination_cup == destination
        # print(cups, f"removed {destination_cup}")
        cups.extendleft([burn_3, burn_2, burn_1, destination_cup])
        # print(cups, "extend")
        cups.rotate(-offset)
        # print(cups, f"rotated {-offset}")
        cups.appendleft(current)
        # print(cups, "append")
        cups.rotate(move)
        # print(cups, "final")


    # print('-- final --')
    # print(f'cups: {" ".join(f" {cup} " for cup in cups)}')
    offset = cups.index(1)
    star_1 = cups[offset+1]
    star_2 = cups[offset+2]

    return star_1 * star_2


def main() -> None:
    # with readfile() as data:
    #     pass
    print(part1("389125467", 10))
    print(part1("389125467", 100))
    print(part1("784235916", 100))
    # print(part2("784235916", 10_000_000))
    # print(part1(data))
    # print(part2(data))


if __name__ == '__main__':
    main()
