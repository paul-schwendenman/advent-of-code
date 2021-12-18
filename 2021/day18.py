import fileinput
from dataclasses import dataclass

@dataclass
class SnailNumber:
	x: int
	y: int

	def __str__(self):
		return f'[{self.x},{self.y}]'

def parse(string):
	print(string)
	raw = eval(string)

	def inner(lst):
		[raw_x, raw_y] = lst

		try:
			x = int(raw_x)
		except:
			x = inner(raw_x)
		try:
			y = int(raw_y)
		except:
			y = inner(raw_y)

		return SnailNumber(x, y)

	return inner(raw)


def reduce(number):
	pass


def add(number_1, number_2):
	return SnailNumber(x=number_1, y=number_2)


def calc_magnitude(number):
	if isinstance(number, int):
		return number

	x, y = number.x, number.y

	if isinstance(x, SnailNumber):
		x = calc_magnitude(x)

	if isinstance(y, SnailNumber):
		y = calc_magnitude(y)

	print(f'{x} * 3 + {y} * 2 = {x * 3 + y * 2}')
	return x * 3 + y * 2


def part1(data):
	pass


def part2(data):
	pass


def main():
    with fileinput.input() as input:
        data = [line.rstrip() for line in input]

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
