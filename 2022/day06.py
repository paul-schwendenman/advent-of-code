import fileinput


def part1(data, size = 4):
	line = list(data)[0]

	for index, _ in enumerate(line):
		if len(set(line[index-size:index])) == size:
			return index


def part2(data):
	return part1(data, size=14)


def main():
	print(part1(fileinput.input()))
	# assert(part1(fileinput.input()) == 1912)
	print(part2(fileinput.input()))
	# assert(part2(fileinput.input()) == 2122)


if __name__ == '__main__':
	main()
