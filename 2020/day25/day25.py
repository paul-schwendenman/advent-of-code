from __future__ import annotations
from typing import Sequence
from aoc import readfile, profiler
from itertools import count


def handshake(subject: int, loop: int) -> int:
    return pow(subject, loop, 20201227)


def brute_force_loop(subject: int, key: int) -> int:
    value = 1
    for index in count(1):
        value *= subject
        value %= 20201227
        if value == key:
            break

    return index


@profiler
def part1(data: Sequence[str]) -> int:
    door_key, card_key = [int(key) for key in data]

    # print('finding door')
    door_loop = brute_force_loop(7, door_key)
    # print(f'found door loop: {door_loop}')
    # print('finding card')
    card_loop = brute_force_loop(7, card_key)
    # print(f'found card loop: {card_loop}')

    enc_key_1 = handshake(door_key, card_loop)
    enc_key_2 = handshake(card_key, door_loop)

    assert enc_key_1 == enc_key_2

    return enc_key_2


@profiler
def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
