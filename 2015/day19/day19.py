from dataclasses import dataclass
import fileinput
from itertools import count
import re

@dataclass
class Replacements:
	reagent: str
	product: str

	def react(self, compound):
		return re.sub('^' + self.reagent, self.product, compound, count=1)

def split_string(string):
	for index in range(len(string)):
		yield string[:index], string[index:]


def parse_substitutions(raw):
	pattern = re.compile(r'([A-Za-z]+) => ([A-Za-z]+)')
	for line in raw:
		if pattern.match(line) is None:
			print(f'no match: "{line}"')
	return [Replacements(*pattern.match(line).groups()) for line in raw]


def part1(raw_substitutions, goal):
	substitutions = parse_substitutions(raw_substitutions)

	results = set()

	# print(substitutions)

	for first, second in split_string(goal):
		for replacement in substitutions:
			results.add(first + replacement.react(second))

	return len(results) - 1


def main():
	lines = list(fileinput.input())

	substitutions, goal = lines[:-2], lines[-1]

	# print(substitutions, goal)
	print(part1(substitutions, goal))
	pass

	# print(list(split_string('HOH')))


if __name__ == '__main__':
	main()