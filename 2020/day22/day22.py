from __future__ import annotations
from typing import Sequence
from aoc import readfile
from collections import deque


def part1(data: Sequence[str]) -> int:
    player_1, player_2 = [deque(int(card) for card in player.split()) for player in '\n'.join(data[1:]).split('\n\nPlayer 2:\n')]

    while len(player_1) > 0 and len(player_2) > 0:
        card_1 = player_1.popleft()
        card_2 = player_2.popleft()

        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        elif card_1 < card_2:
            player_2.append(card_2)
            player_2.append(card_1)

    print(player_1)
    print(player_2)
    if len(player_2) == 0:
        winner = player_1
    else:
        winner = player_2

    return sum((a + 1) * b for a, b in enumerate(reversed(winner)))



def part2(data: Sequence[str]) -> int:
    pass


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
