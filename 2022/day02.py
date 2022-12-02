import fileinput


def part1(data):
	scores = []
	for game in data:
		other, you = game.strip().split(' ')

		if you == 'X': # rock
			if other == 'A': #rock
				scores.append(1 + 3)
			elif other == 'B': #paper
				scores.append(1 + 0)
			elif other == 'C': #sci
				scores.append(1 + 6)
		elif you == 'Y': # pap
			if other == 'A':
				scores.append(2 + 6)
			elif other == 'B':
				scores.append(2 + 3)
			elif other == 'C':
				scores.append(2 + 0)
			pass
		elif you == 'Z':
			if other == 'A':
				scores.append(3 + 0)
			elif other == 'B':
				scores.append(3 + 6)
			elif other == 'C':
				scores.append(3 + 3)
			pass
		else:
			raise ValueError
	pass
	return sum(scores)


def part2(data):
	scores = []
	for game in data:
		other, you = game.strip().split(' ')

		if you == 'X': # lose
			if other == 'A': # rock
				scores.append(3 + 0)
			elif other == 'B': #paper
				scores.append(1 + 0)
			elif other == 'C': #sci
				scores.append(2 + 0)
		elif you == 'Y': # draw
			if other == 'A':
				scores.append(1 + 3)
			elif other == 'B':
				scores.append(2 + 3)
			elif other == 'C':
				scores.append(3 + 3)
			pass
		elif you == 'Z': # win
			if other == 'A':
				scores.append(2 + 6)
			elif other == 'B':
				scores.append(3 + 6)
			elif other == 'C':
				scores.append(1 + 6)
			pass
		else:
			raise ValueError
	pass
	return sum(scores)
	pass


def main():
	print(part1(fileinput.input()))
	print(part2(fileinput.input()))


if __name__ == '__main__':
	main()
