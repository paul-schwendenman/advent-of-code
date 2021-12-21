import fileinput
from itertools import repeat, cycle, product
from collections import Counter, namedtuple
from typing import Mapping
from enum import Enum


State = namedtuple('State', 'player_1_location player_1_score player_2_location player_2_score current_player')


class Player(Enum):
	PLAYER_1 = 1
	PLAYER_2 = 2


def part1(data: list[str]) -> int:
	player_1_location = int(data[0][28:])
	player_2_location = int(data[1][28:])
	print(player_1_location, player_2_location)

	dice = cycle(list(range(1, 101)))

	player_1_score = 0
	player_2_score = 0

	count = 0

	while True:
		rolls = next(dice), next(dice), next(dice)
		count += 3

		print(rolls)
		player_1_location += sum(rolls)
		player_1_location %= 10
		player_1_location = 10 if player_1_location == 0 else player_1_location

		player_1_score += player_1_location

		if player_1_score >= 1000:
			break

		print(player_1_location)
		rolls = next(dice), next(dice), next(dice)
		count += 3

		player_2_location += sum(rolls)
		player_2_location %= 10
		player_2_location = 10 if player_2_location == 0 else player_2_location

		player_2_score += player_2_location

		if player_2_score >= 1000:
			break




	print(player_1_location, player_2_location)
	print(f'scores: {player_1_score}, {player_2_score}')
	print(count)

	return count * min(player_2_score, player_1_score)


def part2(data: list[str]) -> int:
	player_1_location = int(data[0][28:])
	player_2_location = int(data[1][28:])
	player_1_score = 0
	player_2_score = 0
	initial_player = Player.PLAYER_1

	games: Mapping[State, int] = Counter()
	done: Mapping[int, int] = Counter()

	games[State(player_1_location, player_1_score, player_2_location, player_2_score, initial_player)] += 1

	while len(games):
		print(f'games: {len(games)}')
		new_games = Counter()

		for game, quantity in games.items():
			if game.current_player == Player.PLAYER_1:
				all_rolls = product(range(1, 4), range(1, 4), range(1, 4))
				for rolls in all_rolls:
					player_1_location = ((sum(rolls) + game.player_1_location - 1) % 10) + 1

					player_1_score = game.player_1_score + player_1_location

					if player_1_score >= 21:
						done[1] += quantity
					else:
						state = State(player_1_location, player_1_score, game.player_2_location, game.player_2_score, Player.PLAYER_2)
						new_games[state] += quantity
			else:
				all_rolls = product(range(1, 4), range(1, 4), range(1, 4))
				for rolls in all_rolls:
					player_2_location = ((sum(rolls) + game.player_2_location - 1) % 10) + 1

					player_2_score = game.player_2_score + player_2_location

					if player_2_score >= 21:
						done[2] += quantity
					else:
						state = State(game.player_1_location, game.player_1_score, player_2_location, player_2_score, Player.PLAYER_1)
						new_games[state] += quantity

		games = new_games

	print(done)
	return done.most_common()[0][1]


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
