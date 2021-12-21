import fileinput
from itertools import cycle, product
from collections import Counter, namedtuple
from typing import MutableMapping, Tuple
from enum import Enum


BOARD_SPACES = 10


class Player(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2


class State(namedtuple('State', 'player_1_location player_2_location player_1_score player_2_score current_player', defaults=(0, 0, Player.PLAYER_1))):
    def next(self, *, player_1_location=None, player_2_location=None, player_1_score=None, player_2_score=None):
        if player_1_location is None:
            player_1_location = self.player_1_location

        if player_2_location is None:
            player_2_location = self.player_2_location

        if player_1_score is None:
            player_1_score = self.player_1_score

        if player_2_score is None:
            player_2_score = self.player_2_score

        if self.current_player == Player.PLAYER_1:
            current_player = Player.PLAYER_2
        else:
            current_player = Player.PLAYER_1

        return State(player_1_location, player_2_location, player_1_score, player_2_score, current_player)


def parse_player_locations(data: list[str]) -> Tuple[int, int]:
    player_1_location = int(data[0][28:])
    player_2_location = int(data[1][28:])

    return player_1_location, player_2_location


def next_location(current, rolls):
    return ((current + sum(rolls) - 1) % BOARD_SPACES) + 1


def part1(data: list[str]) -> int:
    player_locations = dict(zip(Player, parse_player_locations(data)))
    player_scores = dict(zip(Player, (0, 0)))

    dice = cycle(list(range(1, 101)))

    count = 0

    for current_player in cycle(Player):
        rolls = next(dice), next(dice), next(dice)
        count += 3

        player_locations[current_player] = next_location(player_locations[current_player], rolls)
        player_scores[current_player] += player_locations[current_player]

        if player_scores[current_player] >= 1000:
            break

    return count * min(player_scores.values())


def part2(data: list[str]) -> int:
    player_1_start, player_2_start = parse_player_locations(data)

    games: MutableMapping[State, int] = Counter()
    done: Counter[int] = Counter()

    games[State(player_1_start, player_2_start)] += 1

    while len(games):
        # print(f'games: {len(games)}')
        new_games: MutableMapping[State, int] = Counter()

        for state, quantity in games.items():
            if state.current_player == Player.PLAYER_1:
                all_rolls = product(range(1, 4), range(1, 4), range(1, 4))

                for rolls in all_rolls:
                    player_1_location = next_location(state.player_1_location, rolls)

                    player_1_score = state.player_1_score + player_1_location

                    if player_1_score >= 21:
                        done[1] += quantity
                    else:
                        next_state =  state.next(player_1_location = player_1_location, player_1_score = player_1_score)
                        new_games[next_state] += quantity
            else:
                all_rolls = product(range(1, 4), range(1, 4), range(1, 4))

                for rolls in all_rolls:
                    player_2_location = next_location(state.player_2_location, rolls)

                    player_2_score = state.player_2_score + player_2_location

                    if player_2_score >= 21:
                        done[2] += quantity
                    else:
                        next_state =  state.next(player_2_location = player_2_location, player_2_score = player_2_score)
                        new_games[next_state] += quantity

        games = new_games

    return done.most_common()[0][1]


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
