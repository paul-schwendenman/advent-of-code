import fileinput


def score(letter):
	number = ord(letter)

	if number < ord('a'):
		return 1 + 26 + number - ord('A')
	else:
		return 1 + number - ord('a')


def chunk(iterable, chunk_size=3):
	return [iterable[index:index+chunk_size] for index in range(0, len(iterable), chunk_size)]


def part1(data):
	total = 0
	for rucksack in data:
		size = len(rucksack) // 2

		compartment1, compartment2 = set(rucksack[:size]), set(rucksack[size:])
		duplicate = (compartment1 & compartment2).pop()

		total += score(duplicate)

	return total


def part2(data):
	total = 0
	for group in chunk([line.strip() for line in data]):
		elves = list(map(set, group))

		duplicate = (elves[0] & elves[1] & elves[2]).pop()

		total += score(duplicate)

	return total


def main():
	print(part1(fileinput.input()))
	print(part2(fileinput.input()))


if __name__ == '__main__':
	main()
