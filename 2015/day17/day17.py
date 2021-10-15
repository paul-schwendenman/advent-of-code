import fileinput


def distribute(remainder, containers):
	if remainder == 0:
		return 1
	elif len(containers) == 0 or remainder < 0:
		return 0

	return sum(distribute(remainder - item, containers[(index + 1):]) for index, item in enumerate(containers))


def part1(goal, containers):
	containers = sorted(map(int, containers), reverse=True)

	return distribute(goal, containers)


def main():
	print(part1(150, fileinput.input()))


if __name__ == '__main__':
	main()