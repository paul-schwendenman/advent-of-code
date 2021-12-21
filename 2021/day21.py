import fileinput
from itertools import repeat, cycle


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
	pass


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
