from __future__ import annotations
from typing import Sequence
from aoc import readfile, tracer
from collections import deque


def play_combat(player_1, player_2):

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
        winner_name = '1'
    else:
        winner_name = '2'
        winner = player_2

    return winner_name, winner


@tracer
def play_recursive_combat(player_1, player_2):

    round = 1
    # previous_player_1 = []
    # previous_player_2 = []
    while len(player_1) > 0 and len(player_2) > 0:
        # if player_1 == previous_player_1 and player_2 == previous_player_2:
        #     winner = '1'
        #     break
        card_1 = player_1.popleft()
        card_2 = player_2.popleft()

        print(f'Round {round}: {len(player_1)} >= {card_1} and {len(player_2)} >= {card_2}')

        if len(player_1) >= card_1 and len(player_2) >= card_2:
            winner, _ = play_recursive_combat(player_1.copy(), player_2.copy())
        else:
            winner = '1' if card_1 > card_2 else '2'

        if winner == '1':
            player_1.append(card_1)
            player_1.append(card_2)
        elif winner == '2':
            player_2.append(card_2)
            player_2.append(card_1)
        # previous_player_1 = player_1.copy()
        # previous_player_2 = player_2.copy()
        round += 1

    print(player_1)
    print(player_2)
    if len(player_2) == 0:
        winner = player_1
        winner_name = '1'
    else:
        winner_name = '2'
        winner = player_2

    return winner_name, winner


def part1(data: Sequence[str]) -> int:
    player_1, player_2 = [deque(int(card) for card in player.split()) for player in '\n'.join(data[1:]).split('\n\nPlayer 2:\n')]
    _, winner = play_combat(player_1, player_2)

    return sum((a + 1) * b for a, b in enumerate(reversed(winner)))



def part2(data: Sequence[str]) -> int:
    player_1, player_2 = [deque(int(card) for card in player.split()) for player in '\n'.join(data[1:]).split('\n\nPlayer 2:\n')]
    _, winner = play_recursive_combat(player_1, player_2)

    return sum((a + 1) * b for a, b in enumerate(reversed(winner)))


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
