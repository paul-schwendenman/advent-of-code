import fileinput
from enum import Enum, IntEnum

class Choice(IntEnum):
	ROCK = 1
	PAPER = 2
	SCISSORS = 3

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

class Outcome(IntEnum):
	WIN = 6
	TIE = 3
	LOSS = 0


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
	scores = []
	for game in data:
		you, other = parse_game_part1(game)

		scores.append(score_game(you, other))
	return sum(scores)


def part2(data):
	scores = []
	for game in data:
		other, outcome = game.strip().split(' ')

		if outcome == 'X': # lose
			if other == 'A': # rock
				scores.append(3 + 0)
			elif other == 'B': #paper
				scores.append(1 + 0)
			elif other == 'C': #sci
				scores.append(2 + 0)
		elif outcome == 'Y': # draw
			if other == 'A':
				scores.append(1 + 3)
			elif other == 'B':
				scores.append(2 + 3)
			elif other == 'C':
				scores.append(3 + 3)
			pass
		elif outcome == 'Z': # win
			if other == 'A':
				scores.append(2 + 6)
			elif other == 'B':
				scores.append(3 + 6)
			elif other == 'C':
				scores.append(1 + 6)
			pass
		else:
			raise ValueError
	return sum(scores)


def main():
	print(part1(fileinput.input()))
	print(part2(fileinput.input()))


if __name__ == '__main__':
	main()
