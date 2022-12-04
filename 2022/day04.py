import fileinput


def part1(data):
	count = 0
	for pair in data:
		elves = [[int(item) for item in elf.split('-')] for elf in pair.split(',')]

		if elves[0][0] <= elves[1][0] and elves[0][1] >= elves[1][1]:
			count += 1
		elif elves[1][0] <= elves[0][0] and elves[1][1] >= elves[0][1]:
			count += 1
	return count


def part2(data):
	count = 0
	for pair in data:
		elves = [[int(item) for item in elf.split('-')] for elf in pair.split(',')]

		if set(range(elves[0][0], elves[0][1] + 1)) & set(range(elves[1][0], elves[1][1] + 1)):
			count += 1
	return count


def main():
	print(part1(fileinput.input()))
	print(part2(fileinput.input()))


if __name__ == '__main__':
	main()
