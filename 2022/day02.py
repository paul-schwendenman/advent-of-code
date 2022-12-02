import fileinput
from enum import Enum, IntEnum

class Choice(IntEnum):
	ROCK = 1
	PAPER = 2
	SCISSORS = 3

	def next(self):
		'''Get the Choice which beats self'''
		mapping = {
			Choice.ROCK: Choice.PAPER,
			Choice.PAPER: Choice.SCISSORS,
			Choice.SCISSORS: Choice.ROCK
		}

		return mapping[self]

	def prev(self):
		'''Get the Choice which is beat by self'''
		return self.next().next()

	def __lt__(self, other):
		return other == self.next()

	def __gt__(self, other):
		return other.next() == self


class Outcome(IntEnum):
	WIN = 6
	TIE = 3
	LOSS = 0


def calculate_outcome(you, other):
	if you == other:
		return Outcome.TIE
	if you > other:
		return Outcome.WIN

	return Outcome.LOSS


def score_game(you, other):
	return you + calculate_outcome(you, other)


def score_game_part1(game):
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

	return score_game(your_choice_map[you], other_choice_map[other])


def find_your_choice(other, outcome):
	if outcome == Outcome.TIE:
		return other
	elif outcome == Outcome.WIN:
		return other.next()
	elif outcome == Outcome.LOSS:
		return other.prev()


def score_game_part2(game):
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
	desired_outcome = outcome_map[goal]

	you = find_your_choice(other, desired_outcome)

	return score_game(you, other)


def part1(data):
	return sum(score_game_part1(game) for game in data)


def part2(data):
	return sum(score_game_part2(game) for game in data)


def main():
	print(part1(fileinput.input()))
	print(part2(fileinput.input()))


if __name__ == '__main__':
	main()
