import fileinput
from enum import Enum, IntEnum

class Choice(IntEnum):
	ROCK = 1
	PAPER = 2
	SCISSORS = 3


class Outcome(IntEnum):
	WIN = 6
	TIE = 3
	LOSS = 0


def parse_game_part1(game):
	other, you = game.strip().split(' ')

	other_choice_map = {
		'A': Choice.ROCK,
		'B': Choice.PAPER,
		'C': Choice.SCISSORS
	}

	your_choice_map = {
		'X': Choice.ROCK,
		'Y': Choice.PAPER,
		'Z': Choice.SCISSORS
	}

	return your_choice_map[you], other_choice_map[other]


def find_choice(other, outcome):
	if outcome == Outcome.TIE:
		return other
	elif outcome == Outcome.WIN:
		if other == Choice.ROCK:
			return Choice.PAPER
		elif other == Choice.PAPER:
			return Choice.SCISSORS
		elif other == Choice.SCISSORS:
			return Choice.ROCK
	elif outcome == Outcome.LOSS:
		if other == Choice.SCISSORS:
			return Choice.PAPER
		elif other == Choice.ROCK:
			return Choice.SCISSORS
		elif other == Choice.PAPER:
			return Choice.ROCK


def parse_game_part2(game):
	other, goal = game.strip().split(' ')

	other_choice_map = {
		'A': Choice.ROCK,
		'B': Choice.PAPER,
		'C': Choice.SCISSORS
	}

	outcome_map = {
		'X': Outcome.LOSS,
		'Y': Outcome.TIE,
		'Z': Outcome.WIN
	}

	other = other_choice_map[other]
	you = find_choice(other, outcome_map[goal])

	return you, other


def calculate_outcome(you, other):
	if you == other:
		return Outcome.TIE
	if you == Choice.ROCK and other == Choice.SCISSORS:
		return Outcome.WIN
	if you == Choice.PAPER and other == Choice.ROCK:
		return Outcome.WIN
	if you == Choice.SCISSORS and other == Choice.PAPER:
		return Outcome.WIN

	return Outcome.LOSS


def score_game(you, other):
	return you + calculate_outcome(you, other)


def part1(data):
	return sum(score_game(*parse_game_part1(game)) for game in data)


def part2(data):
	return sum(score_game(*parse_game_part2(game)) for game in data)


def main():
	print(part1(fileinput.input()))
	print(part2(fileinput.input()))


if __name__ == '__main__':
	main()
