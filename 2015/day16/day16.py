from dataclasses import dataclass, fields
import fileinput
import re


@dataclass
class Aunt():
	number: int
	children: int = None
	cats: int = None
	samoyeds: int = None
	pomeranians: int = None
	akitas: int = None
	vizslas: int = None
	goldfish: int = None
	trees: int = None
	cars: int = None
	perfumes: int = None

	def __post_init__(self):
		for field in fields(self):
			value = getattr(self, field.name)
			if not isinstance(value, field.type) and not value is None:
				setattr(self, field.name, field.type(value))

	def matches(self, other):
		for field in fields(self):
			value = getattr(self, field.name)
			other_value = getattr(other, field.name)

			if value is None or other_value is None:
				continue

			if value != other_value:
				return False

		return True



def parse_aunts(lines):
	pattern = re.compile(r'Sue (?P<number>[0-9]+): (?P<kwargs>[a-z]+: [0-9]+, [a-z]+: [0-9]+, [a-z]+: [0-9]+)')

	aunts = []

	for line in lines:
		match = pattern.match(line)

		if match is None:
			raise ValueError("Invalid input data: %s", line)

		number, kwargs = match.groups()

		aunt = dict(item.split(": ") for  item in kwargs.split(", "))
		aunt["number"] = number

		aunts.append(Aunt(**aunt))

	return aunts



def part1(lines):
	aunts = parse_aunts(lines)

	ticker = Aunt(number=None, children=3, cats=7, samoyeds=2, pomeranians=3, akitas=0, vizslas=0, goldfish=5, trees=3, cars=2, perfumes=1)

	for aunt in aunts:
		if aunt.matches(ticker):
			return aunt.number


def main():
	print(part1(fileinput.input()))

if __name__ == '__main__':
	main()