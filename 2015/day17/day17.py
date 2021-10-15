from itertools import chain
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


def distribute2(goal, remaining_containers, used_containers=[]):
	if goal == sum(used_containers):
		return [used_containers]
	elif len(remaining_containers) == 0 or goal < sum(used_containers):
		return []

	return chain.from_iterable(distribute2(goal, remaining_containers[(index + 1):], used_containers + [item]) for index, item in enumerate(remaining_containers))


def part2(goal, containers):
	containers = sorted(map(int, containers), reverse=True)

	combos = list(distribute2(goal, containers))

	shortest = min(map(len, combos))

	return len(list(filter(lambda item: len(item) == shortest, combos)))


def main():
	print(part1(150, fileinput.input()))
	print(part2(150, fileinput.input()))


if __name__ == '__main__':
	main()