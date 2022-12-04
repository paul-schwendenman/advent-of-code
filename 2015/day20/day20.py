from itertools import count
from collections import defaultdict


def part1(goal, gifts_per_elf = 10):
	houses = defaultdict(int)

	for elf in range(1, goal // gifts_per_elf):
		for house in range(elf, goal // gifts_per_elf, elf):
			houses[house] += elf

	for house, score in houses.items():
		if score * gifts_per_elf > goal:
			return house


def part2(goal, gifts_per_elf = 11):
	houses = defaultdict(int)

	for elf in range(1, (goal // gifts_per_elf) + 1):
		for house in range(elf, min(elf * 51, goal // gifts_per_elf), elf):
			houses[house] += elf

	for house, score in sorted(houses.items()):
		if score * gifts_per_elf > goal:
			return house


def main():
	# print(part1(100))
	# print(part1(36000000))
	print(part2(36000000))
	# print(part1(29000000))
	# print(part2(29000000))


if __name__ == '__main__':
	main()
