import fileinput


def part1(data):
	line = list(data)[0]

	for index, char in enumerate(line[3:]):
		# print(set(line[index:index+4]))
		if len(set(line[index:index+4])) < 4:
			continue
		return index + 4
	pass


def part2(data):
	line = list(data)[0]

	for index, char in enumerate(line[13:]):
		# print(set(line[index:index+14]))
		if len(set(line[index:index+14])) < 14:
			continue
		return index + 14
	pass


def main():
	print(part1(fileinput.input()))
	assert(part1(fileinput.input()) == 1912)
	print(part2(fileinput.input()))
	assert(part2(fileinput.input()) == 2122)


if __name__ == '__main__':
	main()
