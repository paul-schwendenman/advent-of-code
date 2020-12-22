from __future__ import annotations
from typing import Sequence, Deque, Tuple
from aoc import readfile, tracer
from collections import deque


def play_combat(player_1: Deque[int], player_2: Deque[int]) -> Tuple[str, Deque[int]]:
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


def play_recursive_combat(player_1: Deque[int], player_2: Deque[int]) -> Tuple[str, Deque[int]]:
    previous_player_1 = []
    previous_player_2 = []
    while len(player_1) > 0 and len(player_2) > 0:
        if tuple(player_1) in previous_player_1 and tuple(player_2) in previous_player_2:
            return '1', player_1
        else:
            previous_player_1.append(tuple(player_1))
            previous_player_2.append(tuple(player_2))

        card_1 = player_1.popleft()
        card_2 = player_2.popleft()

        if len(player_1) >= card_1 and len(player_2) >= card_2:
            winner, _ = play_recursive_combat(deque(list(player_1)[:card_1]), deque(list(player_2)[:card_2]))
        else:
            winner = '1' if card_1 > card_2 else '2'

        if winner == '1':
            player_1.append(card_1)
            player_1.append(card_2)
        elif winner == '2':
            player_2.append(card_2)
            player_2.append(card_1)

    if len(player_2) == 0:
        game_winner = player_1
        winner_name = '1'
    else:
        winner_name = '2'
        game_winner = player_2

    return winner_name, game_winner


def parse_players(data: Sequence[str]) -> Sequence[Deque[int]]:
    return [deque(int(card) for card in player.split()) for player in '\n'.join(data[1:]).split('\n\nPlayer 2:\n')]


def part1(data: Sequence[str]) -> int:
    player_1, player_2 = parse_players(data)

    _, winner = play_combat(player_1, player_2)

    return sum((a + 1) * b for a, b in enumerate(reversed(winner)))


def part2(data: Sequence[str]) -> int:
    player_1, player_2 = parse_players(data)
    name, winner = play_recursive_combat(player_1, player_2)

    return sum((a + 1) * b for a, b in enumerate(reversed(winner)))


def main() -> None:
    with readfile() as data:
        print(part1(data))
        print(part2(data))


if __name__ == '__main__':
    main()
